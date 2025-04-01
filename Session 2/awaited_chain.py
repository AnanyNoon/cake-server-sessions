import asyncio


async def func5():
    print("func5 starting")
    await asyncio.sleep(1)  # Only here does control return to event loop
    print("func5 ending")


async def func4():
    print("func4 starting")
    await func5()  # Direct await - execution flows straight into func5
    print("func4 ending")


async def func3():
    print("func3 starting")
    await func4()  # Direct await - execution flows straight into func4
    print("func3 ending")


async def func2():
    print("func2 starting")
    await func3()  # Direct await - execution flows straight into func3
    print("func2 ending")


async def func1():
    print("func1 starting")
    await func2()  # Direct await - execution flows straight into func2
    print("func1 ending")


async def fun2(index):
    print(f"Task {index}")


async def run():
    await asyncio.gather(*[func1(), fun2(1), fun2(3)])


asyncio.run(run())
