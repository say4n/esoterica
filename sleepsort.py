#! /usr/bin/env python3

import asyncio

MULTIPLIER = 10**-3

async def delaysorthelper(num):
    await asyncio.sleep(num * MULTIPLIER)
    print(num)

async def delaysort(arr):
    tasks = []
    for num in arr:
        t = asyncio.create_task(delaysorthelper(num))
        tasks.append(t)

    for t in tasks:
        await t

if __name__ == "__main__":
    arr = [10, 6, 2, 3, 5, 1, 4]
    asyncio.run(delaysort(arr))
