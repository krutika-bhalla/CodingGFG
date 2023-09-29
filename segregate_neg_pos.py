# segregate_neg_pos.py
# TWO POINTERS

n = int(input())
# k = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    
l,r = 0, len(arr)-1

while l < r:
    # if arr[l] < 0 and arr[r] > 0:
        # continue
    if arr[l] > 0 and arr[r] < 0:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    elif arr[l] < 0 and arr[r] > 0:
        l+=1
    elif arr[l] < 0 and arr[r] < 0:
        l+=1
    elif arr[l] > 0 and arr[l] > 0:
        r-=1
print(arr)