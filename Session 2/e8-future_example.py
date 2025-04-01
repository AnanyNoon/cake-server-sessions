import asyncio


async def run():
    loop = asyncio.get_event_loop()

    future = loop.create_future()
    print(future)
    future.set_result(50)
    print(future)
    res = await future

    print(res)


asyncio.run(run())
