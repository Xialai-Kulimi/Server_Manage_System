import asyncio
import threading

loop = asyncio.get_event_loop()  # 建立一個Event Loop


async def example():  # 定義一個協程
    print("Start example coroutin.")
    # await asyncio.sleep(1)  # 中斷協程一秒
    print("Finish example coroutin.")


def do_loop():
    while True:
        loop.run_until_complete(example())


do_loop_thread = threading.Thread(target=do_loop)
do_loop_thread.start()
print(213213213513513132132135151)


