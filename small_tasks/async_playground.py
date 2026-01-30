import asyncio

async def fetch(i: int) -> str:
    await asyncio.sleep(1)
    return f"ok-{i}"

async def main():
    tasks = [asyncio.create_task(fetch(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())