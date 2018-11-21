#
import random
a = random.sample(range(15),5)
b = random.sample(range(15),10)
print (a)
print (b)
c = [i for i in set(a) if i in b]
print(c)





