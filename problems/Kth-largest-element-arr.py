# https://www.youtube.com/watch?v=FrWq2rznPLQ
# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

arr = [3,2,1,5,6,4, 11, 19, 13]
k = 2
import heapq
large = heapq.nlargest(k, arr)
print(large)
print(large[-1])
