# count the elem to be removed to get the wave array.

arr = [1,0,2,6,3,7]

def up(i, j):
    if i < j: return True
    else: return False
def down(i, j):
    if i > j: return True
    else: return False
 
i = 0
j = 1  
count = 0

# Repeat this code for down array
goup = True
while i < len(arr)-2:
    if goup:
        while j <len(arr) and  not up(arr[i], arr[j]):
            count += 1
            j+=1
        goup = False
    else:
        while j <len(arr) and  not down(arr[i], arr[j]):
            count += 1
            j+=1
        goup = True
    i = j
    j += 1
        
print(count)
