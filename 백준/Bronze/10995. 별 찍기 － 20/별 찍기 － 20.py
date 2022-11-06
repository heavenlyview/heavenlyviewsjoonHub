n = int(input())
s = "*" + " *"*(n-1)
space = False
for i in range(n):
    print(" " + s if space else s)
    space = not space