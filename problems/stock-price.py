# Easier than https://www.geeksforgeeks.org/stock-buy-sell/

price = [100, 180, 260, 310, 40, 535, 695]
min1 = price[0]
max1 = 0

for i in  range(1, len(price)):
    # step 3
    if price[i] < price[i-1]:
        print(min1, max1)
        min1 = price[i]
        max1 = 0
    # step 1
    if price[i]< min1:
        min1 = price[i]
        continue
    # step 2
    if price[i]> max1:
        max1 = price[i]
        continue
        
# step 4. print last.
print(min1, max1)
