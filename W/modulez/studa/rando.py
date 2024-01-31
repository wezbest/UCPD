'''
Testing out the randomizer from tutor
'''

import bussy.lickk as lq
import random


def randoz():
    # for i in range(10):
    #     lq.rprint(random.randint(1, 1000000000))
    return map(lambda _: lq.rprint(random.randint(1, 1000000000)), range(10))


def randoz2():
    """
    Printing random number from 0 to 1 
    """
    return map(lambda _: lq.rprint(random.random()), range(10))


def rando_choice():
    """
    Printing random number from 0 to 1 
    """
    return map(lambda _: lq.rprint(random.choice([1, 2, 3, 4, 5])), range(10))


def rando_shuff():
    """
    Printing a shuffled list of random numbers between 0 and 1
    """
    mylist = [random.random() for _ in range(
        10)]  # Generate a list of random numbers
    lq.rprint(mylist)  # Print the original list

    random.shuffle(mylist)  # Shuffle the list in-place
    lq.rprint(mylist)  # Print the shuffled list
