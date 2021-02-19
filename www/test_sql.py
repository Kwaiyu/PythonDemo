# import www.orm
# import asyncio
# from www.models import User, Blog, Comment
#
# async def test(loop):
#     await www.orm.create_pool(loop=loop, user='root', password='asdasd', db='awesome')
#     u = User(name='Test', email='test@qq.com', passwd='1234567890', image='about:blank')
#     await u.save()
#     www.orm.__pool.close()
#     await www.orm.__pool.wait_closed()
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(test(loop))
#     loop.close()

import asyncio
import www.orm as orm
from www.models import User, Blog, Comment
loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='root', password='asdasd', db='awesome', loop=loop)
    u = User(name='Test01', email='test01@example.com', passwd='1234567890', image='about:blank')
    await u.save()
loop.run_until_complete(test())
loop.close()