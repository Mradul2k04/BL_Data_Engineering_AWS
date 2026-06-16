# MAPPER CODE
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)

for row in reader:
    product= row[0]
    sales = int(row[1])

    print(f"{product}\t{sales}")


# REDUCER CODE
import sys

current_product = None
total_sales = 0

for line in sys.stdin:
    product,sales = line.strip().split("\t")
    sales = int(sales)

    if current_product == product:
        total_sales += sales

    else:
        if current_product:
            print(f"{current_product}\t{total_sales}")

        current_product = product
        total_sales = sales

if current_product:
    print(f"{current_product}\t{total_sales}")