# https://www.geeksforgeeks.org/next-greater-element/

def next_element(arr):
    s = []
    for i in range(len(arr)):
        while s and s[-1].get("value") < arr[i]:
            t = s.pop(-1)
            arr[t.get("ind")] = arr[i]
        
        s.append({"ind":i, "value":arr[i]})
    while s:
        t = s.pop(-1)
        arr[t.get("ind")] = -1
    return arr
arr = [4,5,3,25]
print(next_element(arr)) # [5, 25, 25, -1]
