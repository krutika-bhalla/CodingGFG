n = int(input())
# k = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)
# sorting
# selection sort

for i in range(len(arr)):
    imin = i
    
    for j in range(i+1, len(arr)):
        if arr[j] < arr[imin]:
            imin = j
            
    # if imin != i:
    arr[imin], arr[i] = arr[i], arr[imin]
print(arr)