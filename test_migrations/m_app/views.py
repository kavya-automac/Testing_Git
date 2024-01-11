from django.shortcuts import render

# Create your views here.

def add(a,b):
    c=a+b
    return c
print(add(2,3))

def my_fun():

    print("adding print statement-neeraj")

    print("overriding")

    a=2
    b=3
    c=a*b
    print('c',c,a,b)
    return c
print(my_fun())

print('////////////////////')