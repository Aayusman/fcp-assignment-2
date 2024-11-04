
import sys

n = int(sys.argv[1])

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
   
print(countdown(n))
