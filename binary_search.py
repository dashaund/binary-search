import sys
import random
#import pdb
#pdb.set_trace()

arr = []
ox = 0
nx = 0
for i in range(0,5):
    nx = random.randint(0,100)+ox
    arr.append(nx)
    ox = nx
print(arr)

char = int(sys.argv[1])

low = 0
high = len(arr)-1
mid = int((low + high) / 2)
flag = False

while low != high and flag == False:
    if char > arr[mid]:
        low = mid+1
    elif char < arr[mid]:
        high = mid-1

    if high < 0:
        high = 0

    mid = int((low + high) / 2)
    if char == arr[mid]:
        flag = True

if flag:
    print("Found at position %d" % mid)
else:
    print("Not found")