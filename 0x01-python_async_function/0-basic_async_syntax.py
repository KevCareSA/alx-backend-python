#!/usr/bin/env python3
'''Task 0: The basics of async
Implement an asynchronous coroutine that takes an integer
argument (`max_delay`, default value is 10) named
`wait_random`. This coroutine should wait for a random delay
between 0 and `max_delay` (inclusive, as a float) seconds
and return the generated delay.

Utilize the `random` module for randomness.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds and returns it as a float
    '''
    random_delay: float = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
