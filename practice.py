items = ["milk", "eggs", "bacon", "shirt", "cheese"]
prices = [2.99, 7.99, 6.99, 10.99, 3.99]

for i in range(len(items)): 
    print(f"I bought {items[1]} for ${prices[1]}")
#for index in range(len(items))    
   # print(f"Index: {index} I bought {items[1]} for ${prices[1]}")

total = 0
for t in prices:
    total = total + t
print (f"I spent ${total} at Walmart")


least = prices.index(min(prices))
most = prices.index(max(prices))
print (f"The cheapest item was {items[most]}")
print (f"The most expesnive item was {items[least]}")