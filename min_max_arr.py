# used tournament search
def minmax(low, high, arr):
    arr_min = arr[low]
    arr_max = arr[high]
    
    # arr size = 1
    if low == high:
        return (arr_min, arr_max)
    
    # arr_size = 2
    elif high == low + 1:
        if arr[low] >= arr[high]:
            arr_min = arr[high]
            arr_max = arr[low]
        else:
            arr_min = arr[low]
            arr_max = arr[high]
        return (arr_min, arr_max)
    
    # arr_size > 2
    else:
        mid = (low + high) // 2
        arr_min1, arr_max1 = minmax(low, mid, arr)
        arr_min2, arr_max2 = minmax(mid+1, high, arr)
        
        return (min(arr_min1, arr_min2), max(arr_max1, arr_max2))
    
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    # print(arr)
print(minmax(0, len(arr)-1, arr))
