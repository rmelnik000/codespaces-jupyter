"""hi"""

import random

#print('Good MORNING')

'''x = True

if x > 2:
    print("x is bigger than 2")
elif x < 0:
    print('x is negative')
else:
    print('x is 0, 1, or 2')


september = random.randint(0,10)
print(september)'''

even = 0
odd = 0
bars = 0

while bars < 50:
    value = random.randint(1000,9999)

    if value % 2 == 1:
        print("value is odd")
        odd += 1
    else: 
        print ("value is even")
        even += 1
    print("value is", value)

    print("evens:", even)
    print("odds:", odd)
    bars += 1