import sqlite3

def connect_disconnect(func):
    def decorated(*args, **kwargs):
        global my_connection
        global my_cursor
        my_connection=sqlite3.connect(args[0])
        my_cursor=my_connection.cursor()
        func(*args, **kwargs)
        my_connection.commit()
        my_connection.close()
    return decorated

@connect_disconnect
def create_table( database_name , table_name , table_structure ):
    try:
        my_cursor.execute('''
            CREATE TABLE {} ( {} )
        '''.format(table_name, table_structure))
        #Table created successfully
    except sqlite3.OperationalError:
        #Table already exists
        pass

@connect_disconnect
def insert_record(database_name, record):
    my_cursor.execute(record)

@connect_disconnect
def insert_several_records(database_name, multiple_records):
    for i in multiple_records:
        my_cursor.execute(i)

@connect_disconnect
def read_records(database_name, table_name):
    my_cursor.execute("SELECT * FROM {}".format(table_name))
    records=my_cursor.fetchall()
    return records

@connect_disconnect
def read_last_record(database_name, table_name):
    my_cursor.execute("SELECT * FROM {} ORDER BY ID DESC LIMIT 1".format(table_name))
    records=my_cursor.fetchall()
    return records[0]

@connect_disconnect
def update_record(database_name, record):
    my_cursor.execute(record)

@connect_disconnect
def remove_record(database_name, record):
    my_cursor.execute(record)

@connect_disconnect
def run_command(database_name, command):
    my_cursor.execute(command)

if __name__ == "__main__":
    #Create one Table
    columns = """
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ITEM_NAME VARCHAR(50),
            PRICE INTEGER,
            SECTION VARCHAR(20)"""
    create_table("BaseProducts","TableProducts",columns)

    #Insert one record
    insert_record("BaseProducts","INSERT INTO TableProducts VALUES (NULL,'BALL',10,'SPORT')")
    #Record inserted successfully!

    #Insert several records
    insert_several_records("BaseProducts",[
        "INSERT INTO TableProducts VALUES (NULL,'GOLF STICK',25,'SPORT')",
        "INSERT INTO TableProducts VALUES (NULL,'GLASS',20,'CERAMIC')",
        "INSERT INTO TableProducts VALUES (NULL,'T-SHIRT',5,'CLOTHES')"
    ])
    #Records inserted successfully!

    #Read all records
    list_of_tuples = read_records("BaseProducts","TableProducts")

    #Read last record
    last_record = read_last_record("BaseProducts","TableProducts")

    #Update record
    update_record("BaseProducts","UPDATE TableProducts SET ITEM_NAME='BALL NAME UPDATED' WHERE ID=3")
    #The record with ID=3 has been updated successfully!

    #Remove record
    remove_record("BaseProducts","DELETE FROM TableProducts WHERE ID=3")
    #The record with ID=4 has been removed successfully!
