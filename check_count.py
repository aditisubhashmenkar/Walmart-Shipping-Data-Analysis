import sqlite3

conn = sqlite3.connect("shipment_database.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM product")
print("Products:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM shipment")
print("Shipments:", cursor.fetchone()[0])

conn.close()