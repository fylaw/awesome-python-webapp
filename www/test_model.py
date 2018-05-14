import orm
from models import User, Blog, Comment

import asyncio

async def test():
    await orm.create_pool(loop=loop, user='root', password='', database='awesome')
    u = User(name='y', email='y@test.com', passwd='123456', image='abount:blank')
    await u.save()

print('is test coroutinefunction:', asyncio.iscoroutinefunction(test))

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()