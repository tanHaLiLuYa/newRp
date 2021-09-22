import numpy as np 
m = np.arange(6).reshape(3, 1, 2)
n = np.arange(6).reshape(3, 2, 1)
# print(m,"+++++++++++",n)
# print(m+n)
structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3,2-2j),(3, 'Third', 0.8, 1+3j)],dtype=('int16, a6, float32, complex64'))
print(structured)