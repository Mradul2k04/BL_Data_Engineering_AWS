from faker import Faker
import numpy as np 
import pandas as pd 
import random
import csv

#Initalize Faker
fake=Faker()

# Reproducibility
random.seed(42)
np.random.seed(42)
Faker.seed(42)


#total records
num_records = 1000

#Categories
warehouses = ["WH-A", "WH-B", "WH-C", "WH-D", "WH-E"]

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
    "Router",
    "SSD",
    "Hard Disk"
]

suppliers = [
    "Supplier-X",
    "Supplier-Y",
    "Supplier-Z",
    "Supplier-A",
    "Supplier-B",
    "Supplier-C"
]

# Base transport cost for warehouses
warehouse_cost = {
    "WH-A": 250,
    "WH-B": 500,
    "WH-C": 850,
    "WH-D": 920,
    "WH-E": 1000
}

# Product weight/cost factor
product_cost = {
    "Laptop": 1500,
    "Mobile": 900,
    "Tablet": 1200,
    "Monitor": 1800,
    "Keyboard": 400,
    "Mouse": 250,
    "Printer": 2220,
    "Router": 800,
    "SSD": 6000,
    "Hard Disk": 700
}

# Supplier factor
supplier_factor = {
    "Supplier-X": 150,
    "Supplier-Y": 250,
    "Supplier-Z": 350,
    "Supplier-A": 400,
    "Supplier-B": 200,
    "Supplier-C": 300
}
data = []

for _ in range(num_records):

    warehouse = random.choice(warehouses)
    product = random.choice(products)
    supplier = random.choice(suppliers)

    reorder_level = random.randint(50, 300)

    # 10% chance of missing stock level
    if random.random() < 0.10:
        stock_level = np.nan
    else:
        stock_level = random.randint(20, 600)

    last_updated = fake.date_between(
        start_date="-2y",
        end_date="now"
    )

    # Transport Cost
    transport_cost = (
        warehouse_cost[warehouse]
        + product_cost[product]
        + supplier_factor[supplier]
    )

    transport_cost = round(max(transport_cost, 50), 2)
        
    data.append([
        warehouse,
        product,
        stock_level,
        reorder_level,
        supplier,
        last_updated,
        transport_cost
    ])
# Create DataFrame

df = pd.DataFrame(
    data,
    columns=[
        "Warehouse",
        "Product",
        "Stock Level",
        "Reorder Level",
        "Supplier",
        "Last Updated",
        "Transport Cost"
    ]
)
# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save CSV
df.to_csv("predictive_inventory_dataset.csv", index=False)


print("Dataset Generated Successfully!")
print("\nDataset Shape:", df.shape)
print(df.head())