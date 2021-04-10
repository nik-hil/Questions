# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

meetings = [(15,20),(0,30), (5,10), (35, 40)]
meetings = sorted(meetings, key=lambda x:x[0] )

# [(0,30), (5,10), (15,20), (35, 40)]
start, end = list(zip(*meetings))
# start = [0, 5, 15, 35]
# end = [30, 10, 20, 40]
count = 1
i = 1
j = 0
platform = 0
result = 0
while i < len(start) and j < len(end):
    print(start[i], end[j])
    if start[i] <= end[j]:
        platform += 1
        i += 1
    else:
        platform -= 1
        j += 1
    result = max(platform, result)
print(result)
