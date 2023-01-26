import mysql.connector

def DataUpdate(REGISTRATION,Name,DOB,Address,CELL,CITY,COURSE,EMAIL,GENDER,SCHOOL):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="rasa_feedback"
    )



    mycursor=mydb.cursor()

    #mycursor.execute("DROP TABLE IF EXISTS accommodation_data")

    #sql="CREATE TABLE accommodation_data (REGISTRATION VARCHAR(255),Name VARCHAR(255),DOB VARCHAR(255),Address VARCHAR(255),CELL VARCHAR(255),CITY VARCHAR(255),COURSE VARCHAR(255),EMAIL VARCHAR(255),GENDER VARCHAR(255),SCHOOL VARCHAR(255))"
    sql='INSERT INTO accommodation_data (REGISTRATION,Name,DOB,Address,CELL,CITY,COURSE,EMAIL,GENDER,SCHOOL) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}");'.format(REGISTRATION,Name,DOB,Address,CELL,CITY,COURSE,EMAIL,GENDER,SCHOOL)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"record inserted.")

def DataExtract(REGISTRATION):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="rasa_feedback"
    )

    mycursor = mydb.cursor()
    sql_select_query = "select * from accommodation_data where REGISTRATION =  %s"
    # set variable in query
    mycursor.execute(sql_select_query, (REGISTRATION,))
    myresult = mycursor.fetchall()
    for row in myresult:
        print("Registration= ",row[0], end="\n")
        print("Name=", row[1], end="\n")
        print("DOB=", row[2], end="\n")
        print("CELL= ",row[3], end="\n")
        print("CITY= ", row[4], end="\n")
        print("EMAIL= ", row[5], end="\n")
        print("GENDER= ", row[6], end="\n")
        print("SCHOOL= ", row[7], end="\n")


#if __name__ == '__main__':
  #DataExtract('1')





