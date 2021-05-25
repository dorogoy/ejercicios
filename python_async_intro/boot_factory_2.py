import asyncio
import random
import time
import sys

BOOTS = 0
START_TIME = time.time()


async def make_boot():
    global BOOTS

    manufacturing_time = random.choice([1, 3, 5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1


async def print_secs():
    while True:
        print("seconds: {0:10.2f} boots: {1}".format(time.time() - START_TIME, BOOTS))
        await asyncio.sleep(1)


async def worker():
    while True:
        await make_boot()


async def main(workers_num):
    tasks = []

    for _ in range(workers_num):
        tasks.append(worker())

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    workers_num = int(sys.argv[1:][0])
    loop = asyncio.get_event_loop()
    loop.create_task(print_secs())
    loop.run_until_complete(main(workers_num))
