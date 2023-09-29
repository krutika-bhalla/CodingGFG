n1 = int(input())
# k = int(input())
arr1 = []
for i in range(n1):
    arr1.append(int(input()))
print(arr1)    

n2 = int(input())
# k = int(input())
arr2 = []
for i in range(n2):
    arr2.append(int(input()))
print(arr2)

union_arr = []
# if n2 > n1:
#     arr1, arr2 = arr2, arr1
    
for i in arr1:
    if i not in arr2:
        union_arr.append(i)
    
for i in arr2:
    if i not in union_arr:
        union_arr.append(i)
print(union_arr)