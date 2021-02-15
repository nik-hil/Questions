# https://www.youtube.com/watch?v=DBLUa6ErLKw

ans = []
def backtrack(nums, path):
    if not nums:
        ans.append(path) 
    for x in range(len(nums)):
        backtrack(nums[:x]+nums[x+1:], path+[nums[x]])

backtrack([1,2,3], [])
print(ans)

#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Time Complexity: O(n*n!) 
