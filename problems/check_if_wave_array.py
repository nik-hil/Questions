arr = [1,4,3,5,2,6,7 ]

def up(arr):
    if arr[0] < arr[1]:
        return True
    else :
        return False
        
def down(arr):
    if arr[0] > arr[1]:
        return True
    else :
        return False
 
if up(arr[0:2]):
    upfirst = True
    for i in range(len(arr)-1):
        if upfirst and up(arr[i:i+2]):
            upfirst = False
            continue
        elif not upfirst and down(arr[i:i+2]):
            upfirst = True
            continue
        else:
            print("Not wave array")
            break
elif down(arr[0:2]):
    downfirst = True
    for i in range(len(arr)-1):
        if downfirst and down(arr[i:i+2]):
            downfirst = False
            continue
        elif not downfirst and up(arr[i:i+2]):
            downfirst = True
            continue
        else:
            print("Not wave array")
            break
else:
    print("wave array")
