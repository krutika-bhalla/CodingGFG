# Kadane's Algo

n = int(input())
# k = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

max_sub = arr[0]
curr_sum = 0

for n in arr:
    if curr_sum < 0:
        curr_sum = 0
    curr_sum += n
    max_sub = max(max_sub, curr_sum)
    
print(max_sub)