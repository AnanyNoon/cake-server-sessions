import httpx
import asyncio

URL = "https://jsonplaceholder.typicode.com/todos/1"

"""
Example:
    CPU bound code:
        Is any code that runs on your machine
        
    I/O bound code:
        Code that isn't run on your machine is I/O bound code
        
    1. send request -> CPU bound (blocking code)
    2. process the request -> I/O bound (Non-blocking code)
    3. receive the response -> CPU bound (blocking code)


    10 requests
    10 times 1. send the request
    
    for request in requests:
        await get_response()

    1. fetch_data(1)
    2. client.get(URL)
    3. return response.json()

    4. fetch_data(2)
    5. client.get(URL)
    return response.json()

    fetch_data(3)
    client.get(URL)
    return response.json()

    1. fetch_data(1)
    2. fetch_data(2)
    3. fetch_data(3)
    
    4. client.get(URL)
    5. client.get(URL) Non-blocking code
    6. client.get(URL)
    
    
    4. client.get(URL)


"""


async def fetch_data(index):
    print(f"Start async task: {index}")
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        print(f"Finished async task: {index}")
        return response.json()


async def run():
    await asyncio.gather(*[fetch_data(1), fetch_data(2), fetch_data(3)])


asyncio.run(run())


"""
    event loop:
        container which take tasks
        
    event_loop.add_task(client.get(URL))

"""
