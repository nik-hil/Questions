# https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
arr = [10, 22, 9, 33, 21, 50, 41, 60]

lis = len(arr) * [1]

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j] and lis[j]+1 > lis[i]:
            lis[i] = lis[j] + 1

print(max(lis)) # 5
