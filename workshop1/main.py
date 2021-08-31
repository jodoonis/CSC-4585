from z3 import *

print("Initializing Variables and Solver...\n")
a = Real('a')
b = Int('b')
c = Int('c')
s= Solver()

s.add(c==ToInt(a))
print ("\n1: ", s)
print ("Solving constraints...")
print (s.check())

s.push()
s.add(c==3*b)
print ("\n2: ",s)
print ("Solving constraints...")
print (s.check())

s.push()
s.add(b > c - 50)
print ("\n3: ",s)
print ("Solving constraints...")
print (s.check())