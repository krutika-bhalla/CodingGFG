def reverse_arr(arr):
    
    l,r = 0, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
        
    return arr

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    # print(arr)
print(reverse_arr(arr))