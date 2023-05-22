import asyncio

async def main():
    print('sahal')
    task = asyncio.create_task(foo('somthinggg'))
    await asyncio.sleep(2)
    print('finished')
    await task
    
async def foo(text):
    print(text)
    await asyncio.sleep(2)
    print('teest')
    
if __name__ == '__main__':
    asyncio.run(main())