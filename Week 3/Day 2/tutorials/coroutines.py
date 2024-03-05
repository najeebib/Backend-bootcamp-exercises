import asyncio


async def f():
    return "f"
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r


result = asyncio.run(g())
print(result)



""" async def z():
    return "f"

async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y """


def stuff():
    return "stuff"
 
def py34_coro():
    #Generator-based coroutine, older syntax
    yield from stuff()

async def py35_coro():
    #Native coroutine, modern syntax
    await stuff()