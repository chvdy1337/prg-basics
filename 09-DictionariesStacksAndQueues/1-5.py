countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "USA", "population": 310000000},
    {"name": "Germany", "population": 80000000},
    {"name": "UK", "population": 70000000},
    {"name": "Spain", "population": 45000000},
    {"name": "Japan", "population": 63000000},
]

print("COUNTRY     POPULATION")
for country in countries:
    print(f"{country['name']: <11} {country['population']}")