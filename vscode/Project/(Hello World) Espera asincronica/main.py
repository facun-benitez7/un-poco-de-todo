import asyncio


async def main():
    print('Hello....')
    await asyncio.sleep(2)  # espera 2 segundos
    print('....World!')

asyncio.run(main())
