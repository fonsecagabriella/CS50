

i = 0
while i < 3:
    print ("meow")
    #special sintax for i = i +1 
    i += 1

#another way to do above with lists
for i in [0, 1, 4]:
    #note that the value of i goes in the order they appear in the list
    print("meow")
    print (i) 


#best way to do it
for i in range(23):
    #meows 23 times
    print(f"meow {i}" )

""""
if you are using a variable only for a function you can do this

for _ in range(23):
    #meows 23 times
    print(f"meow {i}" )

MOST SOFISTICATED SOLUTION

while True:
    n = int(input("what is in n?"))
    if n > 0:
        break


for _in range (n):
    print("meow")
"""

#if you want to induce an infinite loop
while True:
    n = int(input("what's n?"))
    if n <0:
        continue
    else:
        break