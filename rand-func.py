from random import *
lst=[1,7,9,13,23,56]

#choice(seq) - returns a random number from a list/tuple/string
print(choice(lst))

#shuffle(seq) - Shuffles the items in a list/tuple.Returns none
print(shuffle(lst))

#randrange([start,] stop [,step]) returns a randomly selected element from range(start,stop,step)
print(randrange(78,98,2))

#random() - returns 0<r<1
print(random())

#seed([x])- sets the startiing value of integer  in generating random nos.This needs to be called before calling any other random module function.
#returns none.
print(seed(6))

#uniform(x,y) - random float x<=r<y
print(uniform(1,9))
