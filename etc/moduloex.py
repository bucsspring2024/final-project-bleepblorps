import pygame

x = 0
y = 10

while x < 100:
    x = x % y #= who cares, what's the remainder
    #event loop
    if x % y ==0:
        print("clicked")
        
    x += 1 #event loop
