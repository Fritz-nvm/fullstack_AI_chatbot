import aioredis

print(aioredis.__version__)

async def test_connection():
    redis = await aioredis.create_redis("redis://localhost") # or whatever redis url you have
    print(redis)
    redis.close()
    await redis.wait_closed()

import asyncio
asyncio.run(test_connection())

print("aioredis imported successfully.")