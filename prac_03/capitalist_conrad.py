import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)


while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)


    price *= (1 + price_change)
    number_of_days += 1


    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)


out_file.close()

#From the random module, we specifically use the randint() function to determine the 50% chance of increase or decrease in price, and the uniform() function to generate a random floating-point number for the price change.
