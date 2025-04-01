import asyncio
import time


async def fn():
    print("Here's your co-routine sir/ma'am")


async def run():
    a = fn()
    print(a)
    time.sleep(5)
    await a


asyncio.run(run())
