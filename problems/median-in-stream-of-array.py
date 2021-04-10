# https://www.youtube.com/watch?v=E-kjYOZEBxY

arr = [3,2,1,5,6,4, 11, 19, 13]

size = 3

temp = []
for a in arr:
    if len(temp) < size:
        temp.append(a)
    del temp[0]
    temp.append(a)
    print(sum(temp)/size)
