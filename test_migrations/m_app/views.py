from django.shortcuts import render

# Create your views here.
def add(a,b):
    c=a+b
    return c
print(add(2,3))