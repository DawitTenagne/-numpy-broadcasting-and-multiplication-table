import numpy as np
#---------------------------------------------------------
ages = np.array([[21,17,65,16,19,33,24,18,33],
                 [15,21,26,99,64,31,17,25,27]])

teenagers = ages[ages < 18]
adults = ages[(ages>=18) & (ages < 65)]
not_adults = ages[(ages<18) | (ages >=65)]
seniors = ages[ages>=65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
#--------------------------------------------------------
print(teenagers)
print(adults)
print(not_adults)
print(seniors)
print(evens)
print(odds)





