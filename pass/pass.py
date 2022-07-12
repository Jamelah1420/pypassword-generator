from lib2to3.pygram import Symbols
from ntpath import join
from random import random
import random 
 
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',',n','o','p','q','r','s','t,','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
Symbols=['!','<','>']

print('Nwlcome to the pypassword generator')
letter=int(input('how many letters would you like in your password?\n'))
Symbol=int(input('how many Symbols would you like in your password?\n'))
number=int(input('how many numbers would you like in your password?\n'))

randomList=[]


for i in range(0,letter):
    n= random.choice(letters)
    randomList.append(n) 


for i in range(0,Symbol):
    n=random.choice(Symbols)
    randomList.append(n)

for i in range(0,number):
    n=random.choice(numbers)
    randomList.append(n)

random.shuffle(randomList)
passwrd="".join(randomList)
print("".join(passwrd))