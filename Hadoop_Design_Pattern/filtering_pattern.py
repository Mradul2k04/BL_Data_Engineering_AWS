# MAPPER CODE 
import sys

for line in sys.stdin:
    order_id,customer, amount = line.strip().split(",")

    if amount != "amount" and int(amount) > 50000:
        print(line.strip())

# REDUCER CODE 
for line in sys.stdin:
    print(line.strip())

# FOR EXECUTING MAP REDUCE CODE 
# cat ecommerce.csv | python3 mapper.py | sort | python3 reducer.py