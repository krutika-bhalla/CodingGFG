n = int(input())
# k = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

lst = arr[-1]
for i in range(len(arr)-1,-1,-1):
    arr[i] = arr[i-1]
arr[0] = lst
print(arr)