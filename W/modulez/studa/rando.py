'''
Testing out the randomizer from tutor
'''

import bussy.lickk as lq
import random


def randoz():
    # for i in range(10):
    #     lq.rprint(random.randint(1, 1000000000))
    return map(lambda _: lq.rprint(random.randint(1, 1000000000)), range(10))
    
def randoz_help():
    return help(random)