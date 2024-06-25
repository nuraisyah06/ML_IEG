'''
Python dictionary is called JSON 
JavaScript Object Notation (JSON)
dictionary also use curly bracket {}
the data is ordered, the data is indexed by key(not by number)
'''

foreigner = {
    "firstname": "Aisyah",
    "lastname": "Razak",
    "passportnumber": "MY8736593" ,
    "incometaxnumber": "MYK237462",
    "pcbamount": 892,
    "lastmonth":5,
    "lastyear":2024,
    "previousmonth": [(4, 2024, 891), (3, 2024, 895), (2, 2024, 895), (1, 2024, 892)],
    "addresses": {
        "office": { 
            "street": "15, Lorong 8/10",
            "taman": "Puchong"
        },
        "home": {
            "street": "215, Jalan SS 8/10",
            "taman": "Subang"
        }
    }
}

print("First Name:", foreigner["firstname"])
print("Last Name:", foreigner["lastname"])
print("Passport Number:", foreigner["passportnumber"])
print("Income Tax Number:", foreigner["incometaxnumber"])
print("PCB Amount:", foreigner["pcbamount"])
print("Last Month:", foreigner["lastmonth"])
print("Last Year:", foreigner["lastyear"])

#for item in foreigner["previousmonth"]:
for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}- {year} RM{amount}")
    
officeAddresses = foreigner["addresses"]["office"]
print("Street:", officeAddresses["street"])
print("Taman:", officeAddresses["taman"])
homeAddresses = foreigner["addresses"]["home"]
print("Street:", homeAddresses["street"])
print("Taman:", homeAddresses["taman"])

print(foreigner["addresses"]["office"]["street"])
print("-" * 50)

print(foreigner.keys())
for key in foreigner.keys():
    if isinstance(foreigner[key], list):
        for item in foreigner[key]:
            print(item)
    else:
        print(foreigner[key])

for key, value in foreigner.items():
    print(key, value)
    
foreigner["car"] ={
    "brand": "Proton",
    "model": "SAGA",
    "carplate": "AIS116"
}
foreigner["salary"] = 4890
print(foreigner)

foreigner["salary"] = 5120
print(foreigner)

foreigner.pop('car')
print(foreigner)