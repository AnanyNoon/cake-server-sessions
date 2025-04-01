from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    import time

    time.sleep(0.1)
    return "hello"
