#!/usr/bin/python3.7

import asyncio

counter = 0
should_print = 1


class Context:
    counter = 0
    should_print = 1


context = Context()


async def print_ones(context):
    while context.should_print == 1:
        if context.counter > 10:
            context.should_print = 0
            continue
        print(1)
        context.counter += 1
        await asyncio.sleep(0.1)


async def print_twos(context):
    while context.should_print == 1:
        if context.counter > 10:
            context.should_print = 0
            continue
        print(2)
        context.counter += 1
        await asyncio.sleep(0.1)


async def print_ones_alt(should_print, counter):
    while should_print == 1:
        if counter > 10:
            should_print = 0
            continue
        print(1)
        counter += 1
        await asyncio.sleep(0.1)

async def print_twos_alt(should_print, counter):
    while should_print == 1:
        if counter > 10:
            should_print = 0
            continue
        print(2)
        counter += 1
        await asyncio.sleep(0.1)


async def program():
    print('Next coros run 5 times every one, since they share a state betwee them')
    await asyncio.gather(
        print_ones(context),
        print_twos(context),
    )

    print('And following coros run 10 times every one, since no shared state between them')
    await asyncio.gather(
        print_ones_alt(should_print, counter),
        print_twos_alt(should_print, counter),
    )

    print(
        'This happens because immutable objects passes by object value (copies created) '
        'and mutable - by object referense (same object uses).'
    )


asyncio.run(program())
