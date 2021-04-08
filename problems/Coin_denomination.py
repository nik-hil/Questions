# https://www.youtube.com/watch?v=jaNZ83Q3QGc&list=RDQMh2jB4IJvwIs&start_radio=1

coins = [1, 2, 5]
amount = 12
combination = [0] * (amount+1)
combination[0]=1
for coin in coins:
    for i in range(len(combination)):
        if i>= coin:
            combination[i] += combination[i-coin]
            
print(combination[-1])
