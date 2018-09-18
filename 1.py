x = 1
y = 1
n = "(N)orth."
N = "n"
s = "(S)outh"
S = "s"
e = "(E)ast"
E = "e"
w = "(W)est"
W = "w"

while True:
    if y == 1:
        change = n
        
    print("You can travel: " , change)
    direct = input("Direction: ")


    if x == 3 and y == 1:
        break


