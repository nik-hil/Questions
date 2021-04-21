# https://www.geeksforgeeks.org/python-program-for-binary-search/
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

arr1 = [5,6,7,10,1,2,3,4,]

def search(arr,l,h, k):
    if h < l:
        return -1
    m = l + (h-l)//2
    
    if arr[m] == k:
        return m
    elif arr[l]< arr[m]:
        if arr[l]<= k<= arr[m]:
            return search(arr,l,m-1, k)
        return search(arr, m+1, h, k)
    else:
        if arr[m]<= k<= arr[h]:
            return search(arr,m+1,h, k)
        return search(arr, l, m-1, k)
       
k = 4 
print(1, search(arr1, 0, len(arr1)-1,k))

