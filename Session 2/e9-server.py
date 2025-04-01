import socket
import select
import queue

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1 << 10

# TCP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

# select lists
read_sockets = [server_socket]
write_sockets = []
message_queues = {}


def delete_socket(sock):
    read_sockets.remove(sock)
    if sock in write_sockets:
        write_sockets.remove(sock)
    sock.close()
    del message_queues[sock]


def accept():
    client_socket, _ = server_socket.accept()
    read_sockets.append(client_socket)
    message_queues[client_socket] = queue.Queue()


def recv(sock):
    return sock.recv(BUFFER_SIZE)


def send(sock, msg):
    sock.send(msg)


print(f"Server listening on {HOST}:{PORT}")

while True:
    # Wait for sockets to be ready
    readable, writable, _ = select.select(read_sockets, write_sockets, [])

    for sock in readable:
        if sock == server_socket:
            accept()
        else:
            data = recv(sock)  # Receive data from client
            if data:
                print(f"Received : {data.decode()} from {sock.getpeername()}")
                response = f"Echo : {data.decode()}"

                message_queues[sock].put(
                    response.encode()
                )  # pushing data to the client

                if sock not in write_sockets:
                    write_sockets.append(sock)
            else:
                # Client disconnected
                print(f"Client {sock.getpeername()} disconnected")

                delete_socket(sock)

    for sock in writable:
        try:
            next_message = message_queues[sock].get_nowait()
        except queue.Empty:
            write_sockets.remove(sock)
        else:
            send(sock, next_message)
