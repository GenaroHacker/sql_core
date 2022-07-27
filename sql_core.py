import sqlite3

def CreateTable( DATABASE_NAME , TABLE_NAME , TABLE_STRUCTURE ):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute('''
        CREATE TABLE ''' + TABLE_NAME + ''' ( ''' + TABLE_STRUCTURE + ''' )
    ''')
    myConnection.commit()
    myConnection.close()

def InsertRecord(DATABASE_NAME, RECORD):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute(RECORD)
    myConnection.commit()
    myConnection.close()

def InsertSeveralRecords(DATABASE_NAME, MULTIPLE_RECORDS):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    for i in MULTIPLE_RECORDS:
        myCursor.execute(i)
    myConnection.commit()
    myConnection.close()

def ReadRecords(DATABASE_NAME, TABLE_NAME):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute("SELECT * FROM " + TABLE_NAME)
    records=myCursor.fetchall()
    myConnection.close()
    return records

def ReadLastRecord(DATABASE_NAME, TABLE_NAME):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute("SELECT * FROM " + TABLE_NAME + " ORDER BY ID DESC LIMIT 1")
    records=myCursor.fetchall()
    myConnection.close()
    return records[0]

def UpdateRecord(DATABASE_NAME, RECORD):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute(RECORD)
    myConnection.commit()
    myConnection.close()

def RemoveRecord(DATABASE_NAME, RECORD):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute(RECORD)
    myConnection.commit()
    myConnection.close()

def RunCommand(DATABASE_NAME, COMMAND):
    myConnection=sqlite3.connect(DATABASE_NAME)
    myCursor=myConnection.cursor()
    myCursor.execute(COMMAND)
    myConnection.commit()
    myConnection.close()



if __name__ == "__main__":
    #Create one Table
    try:
        columns = """
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ITEM_NAME VARCHAR(50),
                PRICE INTEGER,
                SECTION VARCHAR(20)"""
        CreateTable("BaseProducts","TableProducts",columns)
        print("Table created successfully!\n")
    except sqlite3.OperationalError:
        print("Table already exists!!!!\n")


    #Insert one record
    InsertRecord("BaseProducts","INSERT INTO TableProducts VALUES (NULL,'BALL',10,'SPORT')")
    print("Record inserted successfully!\n")


    #Insert several records
    InsertSeveralRecords("BaseProducts",[
        "INSERT INTO TableProducts VALUES (NULL,'GOLF STICK',25,'SPORT')",
        "INSERT INTO TableProducts VALUES (NULL,'GLASS',20,'CERAMIC')",
        "INSERT INTO TableProducts VALUES (NULL,'T-SHIRT',5,'CLOTHES')"
    ])
    print("Records inserted successfully!\n")


    #Read all records
    list_of_tuples = ReadRecords("BaseProducts","TableProducts")
    print("The list of tuples with all the records is:")
    print(list_of_tuples)


    #Read last record
    last_record = ReadLastRecord("BaseProducts","TableProducts")
    print("\nThe last record is:")
    print(last_record)


    #Update record
    UpdateRecord("BaseProducts","UPDATE TableProducts SET ITEM_NAME='BALL NAME UPDATED' WHERE ID=3")
    print("\nThe record with ID=3 has been updated successfully!\n")


    #Remove record
    RemoveRecord("BaseProducts","DELETE FROM TableProducts WHERE ID=3")
    print("The record with ID=4 has been removed successfully!\n")