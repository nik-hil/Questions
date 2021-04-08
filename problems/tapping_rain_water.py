# https://www.geeksforgeeks.org/trapping-rain-water/
# space o(1) , time o(n)
# Simplified by me

def findWater(arr, n):
    result = 0
    left_max = 0
    right_max = 0
    lo = 0
    hi = n-1
    
    while(lo <= hi):
    
        if(arr[lo] < arr[hi]):
            left_max = max(left_max, arr[lo])
            result += left_max - arr[lo]
            lo+= 1
        else:
            right_max = max(right_max, arr[hi])
            result += right_max - arr[hi]
            hi-= 1
        
    return result

# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)

print("Maximum water that can be accumulated is ",
        findWater(arr, n))

