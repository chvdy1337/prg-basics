price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for item, number in price_list.items():
    print (f"{item}: {number*0.9:.2f}")

total = 0
for item, number in price_list.items():
    total += number*0.9
    
print (f"Total Value: {total:.2f}")