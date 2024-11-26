products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}


for name, number in products.items():
    print(f"{name}: {number}")
total = 0
for name, number in products.items():
    total += number

print(f"Total Number Of Prodcts: {total}")