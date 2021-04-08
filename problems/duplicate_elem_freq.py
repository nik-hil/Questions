arr = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3]

cnt = 1
elem = arr[0]
for i in range(1, len(arr)):
    if elem == arr[i]:
        cnt += 1
    else:
        print(elem, " : ", cnt)
        cnt = 1
        elem = arr[i]
print(elem, " : ", cnt)
