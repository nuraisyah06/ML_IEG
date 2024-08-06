from os.path import exists
import mysql.connector as mysql

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if(value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    
    return value

def doMenu(connection):
    choice = -1
    while (choice != 0):
        print("******************************")
        print(":    0 - Exit                :")
        print(":    1 - List of The Product :")
        print(":    2 - Add Product         :")
        print(":    3 - Edit Product        :")
        print(":    4 - Delete Product      :")
        print("******************************")

        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be integer")
        if (choice == 0):
            print("Thank You for using our system")
        elif (choice == 1):
            printProduct(connection)
        elif (choice == 2):
            addProduct(connection)
        elif (choice == 3):
            editProduct(connection)
        elif (choice == 4):
            deleteProduct(connection)
             
def dbConnect():
    connection = mysql.connect(
        host="localhost", user="root", password="", database="Peneraju")
    return connection
        
#content = input("Fruit Name: ")
#filehandler = open(filename, '')
def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write( "Product | Quantity | Price")
            # pipe (|) is use ad delimiter/seperator
            # to split line into multiple data
    except Exception as e:
        print("Header cannot be created, something went wrong", e)    

def addProduct(connection):
    try:
        name = keyboardInput(str, "Product: ", "Product must be string")
        description = keyboardInput(str, "Description: ", "Description must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")
        
        SQL = f"""INSERT INTO PRODUCTS (name, description, quantity, price) 
        VALUES ('{name}','{description}','{quantity}','{price}')"""
        
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit() 
    except Exception as e:
        print("Cannot add the product, something went wrong", e)

def printProduct(connection): 
    SQL = f"SELECT * FROM products"             # or SELECT id,name,description,quantity,price FROM products
    cursor = connection.cursor()
    cursor.execute(SQL)
    print("+-----+--------------------+------------------------------+--------------------+--------------------+")
    print(f"|{'Id':5s}|{'Name':20s}|{'Description':30s}|{'Quantity':20s}|{'Price':20s}|")
    print("+-----+--------------------+------------------------------+--------------------+--------------------+")
    for id,name,description,quantity,price in cursor:
        print(f"|{id:5d}|{name:20s}|{description:30s}|{quantity:20d}|{price:20.2f}|")
    print("+-----+--------------------+------------------------------+--------------------+--------------------+")
        
def editProduct(filename):
    try:
        id = keyboardInput(int, "Product ID to edit: ", "Index must be Integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        
        cursor = connection.cursor()
        cursor.execute(SQL)    
        id, name, description, quantity, price = cursor.fetchone()
        
    except:
        print("Product for this ID not exists")    
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\n Price: {price}")
        
        confirm = keyboardInput(str, f"Do you want to edit this product? [y/n]: ", "Reponse must be in string (YES = Y/y or NO = N/n)")
        
        if (confirm == "y" or confirm == "Y"):
            newproduct = keyboardInput(str, f"Product[{name}]: ", "Product must be string", name)
            newdescription = keyboardInput(str, f"Description[{description}]: ", "Description must be string", description)
            newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be integer", quantity)
            newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float", price)
            
            SQL = f"""UPDATE products SET name='{newproduct}', description='{newdescription}',
                        quantity='{newquantity}', price='{newprice}' WHERE id ={id}"""
                        
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit() 

def deleteProduct(filename):
    try:
        id = keyboardInput(int, "Product ID to edit: ", "Index must be Integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        
        cursor = connection.cursor()
        cursor.execute(SQL)    
        id, name, description, quantity, price = cursor.fetchone()
        
    except:
        print("Product for this ID not exists")    
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\n Price: {price}")
        
        confirm = keyboardInput(str, f"Do you want to edit this product? [y/n]: ", "Reponse must be in string (YES = Y/y or NO = N/n)")
        
        if (confirm == "y" or confirm == "Y"):
            SQL = f"""UPDATE products WHERE id ={id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit() 
            print("Product deleted")
connection = dbConnect()
doMenu(connection)