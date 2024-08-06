
'''
1. x create file if it is not exist
2. t a text file
3. b a binary file
4. w to write inside file, will replace the existing content
'''

'''if exists(filename):
    pass
else:
    open(filename, 'xt')'''

#open('fruits.txt', 'xt')

from os.path import exists

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

def doMenu(filename):
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
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)
             
def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("File cannot be created, something went wrong", e)
        else:
            createTitle(filename)
        finally:
            filehandler.close()
        
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

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Cannot add the product, something went wrong", e)

def printProduct(filename):    
    try:
        #lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
            
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            
            if (index == 0):                
                print("=" * 80)
                print(f"{"No." :5}{product:40}{quantity:>20}{price:>20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
                
    except Exception as e:
        print("Product list cannot be printed, something went wrong", e)
        
def editProduct(filename):
    try:
        line = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Enter No. of the item to edit:", "Index must be integer")
        if (index >= len(lines)):
            print("Sorry product No. doesn't exist")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\n Price: {price}")
            confirm = keyboardInput(str, f"Do you want to edit this product? [y/n]: ", "Reponse must be in string (YES = Y/y or NO = N/n)")
            if (confirm == "y" or confirm == "Y"):
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be string", product)
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be integer", quantity)
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float", price)
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line = "|".join(map(str,product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
                
    except Exception as e:
        print("Cannot edit product, something went wrong," , e)

def deleteProduct(filename):
    try:
        line = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Enter No. of the item to edit:", "Index must be integer")
        if (index >= len(lines)):
            print("Sorry product No. doesn't exist")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\n Price: {price}")
            confirm = keyboardInput(str, f"Do you want to delete this product? [y/n]: ", "Reponse must be in string (YES = Y/y or NO = N/n)")
            if (confirm == "y" or confirm == "Y"):
                del data[index]
                newlines = []
                for product in data:
                    line = "|".join(map(str,product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
                
    except Exception as e:
        print("Cannot edit product, something went wrong," , e)


filename = "cafe.txt"

createFile(filename)
doMenu(filename)
#addProduct(filename)
#printProduct(filename)