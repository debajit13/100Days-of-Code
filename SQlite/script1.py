import sqlite3

def create_table():
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert("Coffee Cup",10,5)
#insert("Tea Cup",12,6)
#insert("Juice Mug",11,7)

def view():
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    return rows

def delete(item):
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close()
update(4,12.4,"Coffee Cup")     #for updating item data
delete("Tea Cup")  #for deleting any item data
print(view())
