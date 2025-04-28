#!/usr/bin/env python3
"""
wait_random function
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function that waits for a random delay between 0 and max_delay
    seconds and eventually returns it"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return (time)
