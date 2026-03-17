##reverse number by While Loop
import os
os.system("cls")


n=9572
rev=0
while n>0:
    rev=n%10
    print(rev,end="")
    n=n//10


