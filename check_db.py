import sqlite3

conn = sqlite3.connect("shipment_database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables:")
for table in tables:
    print(table[0])

for table in tables:
    print(f"\nSchema for {table[0]}:")
    cursor.execute(f"PRAGMA table_info({table[0]})")
    for col in cursor.fetchall():
        print(col)

conn.close()