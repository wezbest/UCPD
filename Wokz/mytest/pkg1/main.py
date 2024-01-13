#!/usr/bin/env python3.12

'''
Testing out multi python files thing
'''

import numpy as np
import func1 as fu # Here we imported that file and its function

data = [12,22,33,44,55]

avgN = np.average(data)

fu.fnc1()
print('Average PussySmell: ',avgN)
