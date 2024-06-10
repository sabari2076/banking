import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="banking"
)
n=int(input("1.new account 2.old account"))
if(n==1):
    name=input("enter customer name")
    phno=int(input("enter phone number"))
    balance=int(input("enter deposit amount"))
    adharno=int(input("enter adhar no"))
    panno=int(input("enter pan no"))
    import random
    passlen=5
    s="1234567890"
    accno=" ".join(random.sample(s,passlen))
    mycursor=mydb.cursor()
    sql="insert into HDFC(name,phno,accno,adharno,panno,balance)values(%s,%s,%s,%s,%s,%s)"
    val=(name,phno,accno,adharno,panno,balance)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"account opening successfully")
if(n==2):
    n=int(input("1.deposit 2.withdraw 3,balance "))
    balance=10000
    count=1
    mycursor=mydb.cursor()
    accno=int(input("enter a account number"))
    sql="select balance from HDFC where accno='{}'",format(accno)
    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    b=myresult[0]
    deposit=int(input("enter deposit amount"))
    v="update HDFC set balance='{}' where accno='{}'",format(b+deposit,accno)
    mycursor.execute(v)
    mydb.commit()
    balance=deposit+balance
    print("deposit:%d",deposit)
elif(n==2):
    mycursor=mydb.cursor()
    accno = int(input("enter a account number"))
    sql="select balance from HDFC where accno='{}'",format(accno)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    v = myresult[0]
    withdraw=int(input("enter withdraw amount"))
    w="update HDFC set balance='{}' where accno='{}",format((v-withdraw,accno))
    mycursor.execute(w)
    mydb.commit()
elif(n==3):
    mycursor = mydb.cursor()
    accno = int(input("enter a account number"))
    sql = "select balance from HDFC where accno='{}'", format(accno)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    h = myresult[0]
    print("account balance",h)



