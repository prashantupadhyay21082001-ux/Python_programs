import mysql.connector

conn=mysql.connector.connect(
    host ="127.0.0.1",
    port = 3306,
    database = 'store',
    user = 'root',
    password = '1234'
)
 
cur = conn.cursor()

# a method addcustomer information
def addcustomer():
    cid=input("enter customer id :")
    cname = input("\tenter customer name:")
    cadd = input("\tenter customer address:")
    cmob= input("\tenter customer mobile:")
    data= (cid,cname,cadd,cmob)
    query="insert into customer(cid,cname,cadd,cmob) value(%s,%s,%s,%s)"
    try:
        cur.execute(query,data)
        if cur.rowcount>0:
            print("\n\tcustomer add successfully")
        else:
            print("\n\tfailed to add customer")
        conn.commit()
    except:
        print("\n\tfailed to execute this query")
    input("\tpress enter to continue...")

# a method to view all customer's information
def viewallcustomer():
    query = "select * from customer"
    cur.execute(query)
    data=cur.fetchall()
    for cus in data:
        print("\n\tenter customer id:", cus[0])
        print("\n\tenter customer name:", cus[1])
        print("\n\tenter customer address:", cus[2])
        print("\n\tenter customer mobile:", cus[3])
        print("\t---------------------------------")
    input("\n\tpress enter to continue..")


    # a method to delete a customer information

def deleteacustomer():
        cid= input("\n\tenter customer id:")
        query= "select * from customer where cid =" +cid
        cur.execute(query)
        data = cur.fetchone()
        if data != None:
            print("\n\tcustomer name:",data[1])
            print("\n\tcustomer address:", data[2])
            query = "delete from customer where cid="+cid
            cur.execute(query)
            if cur.rowcount>0:
                print("\n\tcustomer deleted successfully!")
            else:
                print("\n\tcustomer deletion failed")
            conn.commit()
        else:
            print("\n\t customer not found")    
        input("\n\tpress enter to continue...")



# A method to add product information
def addproduct():
    pid = input("\n\tenter product id:")
    pname =input("\n\tenter product name:")
    price=input("\n\tenter product price:")
    data =(pid,pname,price)
    query="insert into product(pid,pname,price)value(%s,%s,%s)"
    try:
        cur.execute(query,data)
        if cur.rowcount>0:
            print("\n\tproduct added successfully")
        else:
            print("\n\tproduct failed to add")
        conn.commit()
    except Exception as e:
        print("\n\tfailed to execute the query !\n",e)
    input("\n\tpress enter to continue...")


# a method view all product information
def viewallproduct():
    query= "select*from product"
    cur.execute(query)
    data= cur.fetchall()
    for pro in data:
        print("\n\tproduct id:",pro[0])
        print("\n\t product name", pro[1])
        print("\n\tproduct price ", pro[2])
    input("\n\tpress enter to continue...")

# A method update product information
def updateproduct():
    pid = input("\n\tenter product id:")
    query= "select * from product where pid="+pid
    cur.execute(query)
    pro=cur.fetchone() 
    if pro!=None:
        print("\n\tproduct name:", pro[1])
        print("\n\tproduct old price:", pro[2])
        pprice= input("\n\tenter new price:")
        query= "update product set price= %s  where pid= %s"
        data = (pprice,pid)
        cur.execute(query,data)
        conn.commit()
        if cur.rowcount>0:
            print("\n\tprice updated successfully!")
        else:
            print("\n\tunable to update price right now")
    else:
        print("\n\tproduct is not available on this id")
    input("\n\tpress enter to continue...")


# A method to place an order to information
def placeanorder():
    cid = input("\n\tenter customer id:")
    query= "select * from customer where cid="+cid
    cur.execute(query)
    cus= cur.fetchone()
    if cus!= None:
        print("\n\tcustomer name:",cus[1])
        print("\n\tcustomer address:", cus[2])
        pid= input("\n\tenter product id:")
        query= "select * from product where pid="+pid
        cur.execute(query)
        pro= cur.fetchone()
        if pro!=None:
            print("\n\tproduct name:",pro[1])
            print("\n\tproduct price:",pro[2])
            qyt=input("\n\tenter quantity:")
            q="insert into orders(cid,pid,qyt)value(%s,%s,%s)"
            data= (cid,pid,qyt)
            cur.execute(q,data)
            conn.commit()
            print("\n\ttotal bill:", int(qyt)*int(pro[2]))
            if cur.rowcount<0:
                print("\n\torder placed successfully")
            else:
                print("\n\torder placed not successfully")
        else:
            print("\n\tproduct not found")
    else:
        print("\n\tcustomer not found")
    input("\n\tpress enter to continue.....")

# A method to view all order to information
def viewallorders():
    cid=input("\n\tenter customer id:")
    query= "select customer.*,pname,price,qyt from customer join orders using(cid) join product using(pid) where cid="+cid
    cur.execute(query)
    data= cur.fetchall()
    for order in data:
        print("\n\tcustomer id:", order[0])
        print("\n\tcustomer name:", order[1])
        print("\n\tcustomer address:",order[2])
        print("\n\tcustomer mobile:",order[3])
        print("\n\tproduct name:", order[4])
        print("\n\tproduct price:",order[5])
        print("\n\tproduct quantity:", order[6])
        print("\n\ttotal bill:",int(order[5])*int(order[6]))
        print("\t--------------------------------------------")
    input("\n\tpress enter to continue...")

    
# A method to view all customer by cid information
def viewOrderbycid():
    cid=input("\n\tenter customer id:")
    query="select customer.*,pname,price,qyt from customer join orders using(cid) join product using(pid)where cid="+cid
    cur.execute(query)
    data= cur.fetchall()
    for order in data:
        print("\n\tcustomer id:", order[0])
        print("\n\tcustomer name:",order[1])
        print("\n\tcustomer address:", order[2])
        print("\n\tcustomer mobile:", order[3])
        print("\n\tproduct name:", order[4])
        print("\n\tproduct price:", order[5])
        print("\n\tproduct qyt:",order[6])
        print("\n\ttotal bill:", int(order[5]*int(order[6])))
        print("\t---------------------------------------------")
    input("\n\tpress enter to continue.....")

    
    





while True:
    print("\tstore management system")
    print("""   
        1. add customer
        2. view all customer
        3. delete a customer
        4. add product
        5. view all product
        6. update product
        7. place an order
        8. view all orders
        9. view all orders by cid
        0. exit 
    """)
    ch = int(input("enter your choice:"))
    if ch==0:
        print("\n\tthank you for using our software")
        break
    elif ch==1:
        addcustomer()
    elif ch==2:
        viewallcustomer()
    elif ch==3:
        deleteacustomer()
    elif ch==4:
        addproduct()
    elif ch==5:
        viewallproduct()
    elif ch==6:
        updateproduct()
    elif ch==7:
        placeanorder()
    elif ch==8:
        viewallorders()
    elif ch==9:
        viewOrderbycid()




    
        
