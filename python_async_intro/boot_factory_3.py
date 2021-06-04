import asyncio
import random
import sys
import time

BOOTS = 0
START_TIME = time.time()


async def make_boot():
    global BOOTS

    manufacturing_time = random.choice([1, 3, 5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1


async def print_secs():
    while True:
        printable_time = time.time() - START_TIME
        secs_to_wait = 1
        print("seconds: {0:10.2f} boots: {1}".format(printable_time, BOOTS))
        micro_seconds = printable_time % 1
        if micro_seconds:
            secs_to_wait -= micro_seconds
        await asyncio.sleep(secs_to_wait)


async def worker():
    while True:
        await make_boot()


async def workers(workers_num):
    tasks = []
    for _ in range(workers_num):
        tasks.append(worker())

    await asyncio.gather(*tasks)


async def main(workers_num):
    await asyncio.gather(print_secs(), workers(workers_num))


if __name__ == "__main__":
    workers_num = int(sys.argv[1:][0])
    asyncio.run(main(workers_num=workers_num))
