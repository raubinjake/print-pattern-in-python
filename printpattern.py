n = int(input("Enter times of number for pattern "))
b =input("Enter true or false for two types of pattern ")
i=1
if b=="true":
    while(i <= n):
        print("* "*i)
        i=i+1
else:
    while(n > 0):
        print("  "*(i-1),end="")
        print("* "*n)
        i=i+1
        n = n-1