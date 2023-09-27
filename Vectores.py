import  pandas as pd
import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
test = pd. DataFrame ({
'A': [9,2,3,8,1,7],
'B': [5,3,1,7,4,6],
'C': [2,3,7,4,9,1],
'D': [6,3,8,5,0,7],
'E': [1,9,4,3,2,8],
'F': [3,5,2,8,1,7],
'H': [7,3,0,5,2,9],
'I': [8,3,1,7,2,4],
})
test.index =['Year1','Year2','Year3','Year4', 'Year5', 'Year6']
ax = test.plot.bar(rot=0)
print(test)
