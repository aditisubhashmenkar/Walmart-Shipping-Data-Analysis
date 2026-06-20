import pandas as pd
import sqlite3

# Load CSV files
df0 = pd.read_csv("shipping_data_0.csv")
df1 = pd.read_csv("shipping_data_1.csv")
df2 = pd.read_csv("shipping_data_2.csv")

# Connect database
conn = sqlite3.connect("shipment_database.db")
cursor = conn.cursor()

product_ids = {}

def get_product_id(product_name):
    if product_name in product_ids:
        return product_ids[product_name]

    cursor.execute("SELECT id FROM product WHERE name = ?", (product_name,))
    result = cursor.fetchone()

    if result:
        product_id = result[0]
    else:
        cursor.execute(
            "INSERT INTO product (name) VALUES (?)",
            (product_name,)
        )
        product_id = cursor.lastrowid

    product_ids[product_name] = product_id
    return product_id


# Spreadsheet 0
for _, row in df0.iterrows():
    product_id = get_product_id(row["product"])

    cursor.execute("""
        INSERT INTO shipment
        (product_id, quantity, origin, destination)
        VALUES (?, ?, ?, ?)
    """, (
        product_id,
        int(row["product_quantity"]),
        row["origin_warehouse"],
        row["destination_store"]
    ))


# Spreadsheet 1 + 2

merged = pd.merge(
    df1,
    df2,
    on="shipment_identifier"
)

grouped = merged.groupby(
    [
        "shipment_identifier",
        "product",
        "origin_warehouse",
        "destination_store"
    ]
).size().reset_index(name="quantity")

for _, row in grouped.iterrows():
    product_id = get_product_id(row["product"])

    cursor.execute("""
        INSERT INTO shipment
        (product_id, quantity, origin, destination)
        VALUES (?, ?, ?, ?)
    """, (
        product_id,
        int(row["quantity"]),
        row["origin_warehouse"],
        row["destination_store"]
    ))

conn.commit()
conn.close()

print("Database populated successfully!")