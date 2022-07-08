from cs50 import get_float

change = 0

while change <= 0:
    change = get_float("Change owed?:")

#round float and convert input into whole number for easy math
change = round(change * 100)

#declare change denominations and values
quarters = 25
dimes = 10
nickels = 5
pennies = 1

#declare varibles
coins = 0


while quarters in range(change+1):
    change = change - quarters
    coins += 1

while dimes in range(change+1):
    change = change - dimes
    coins += 1

while nickels in range(change+1):
    change = change - nickels
    coins += 1

while pennies in range(change+1):
    change = change - pennies
    coins += 1

print(f"Coin Amount:{coins}");



