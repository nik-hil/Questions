# https://www.geeksforgeeks.org/python-program-for-binary-search/
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

arr1 = [5,6,7,10,1,2,3,4,]

def find_pivot(arr, l, h):
    if not arr:
        return -1
    if h < l:
        return -1
    if l == h:
        return l
    m = l + (h-l)//2
    
    if arr[l] < arr[m]:
        return find_pivot(arr, m, h)
    else:
        return find_pivot(arr, l, m)
        
def search(arr,l,h, k):
    if h <= l:
        return -1
    m = l + (h-l)//2
    
    if arr[m] == k:
        return m
    elif k < arr[m]:
        return search(arr,l,m-1, k)
    else:
        return search(arr,m+1,h, k)
        
pivot = find_pivot(arr1, 0, len(arr1))
k = 7
print(1, search(arr1, 0, pivot,k))
print(2, search(arr1,pivot,len(arr1), k))
