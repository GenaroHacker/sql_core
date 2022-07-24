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

    columns = """
            ARTICLE_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
            ITEM_NAME VARCHAR(50),
            PRICE INTEGER,
            SECTION VARCHAR(20)"""
    CreateTable("BaseProducts","TableProducts",columns)

    InsertRecord("BaseProducts","INSERT INTO TableProducts VALUES (NULL,'BALL',10,'SPORT')")

    InsertSeveralRecords("BaseProducts",[
        "INSERT INTO TableProducts VALUES (NULL,'GOLF STICK',25,'SPORT')",
        "INSERT INTO TableProducts VALUES (NULL,'GLASS',20,'CERAMIC')",
        "INSERT INTO TableProducts VALUES (NULL,'T-SHIRT',5,'CLOTHES')"
    ])

    list_of_tuples = ReadRecords("BaseProducts","TableProducts")
    print(list_of_tuples)

    UpdateRecord("BaseProducts","UPDATE TableProducts SET ITEM_NAME='BALL NAME UPDATED' WHERE ARTICLE_CODE=3")

    RemoveRecord("BaseProducts","DELETE FROM TableProducts WHERE ARTICLE_CODE=3")