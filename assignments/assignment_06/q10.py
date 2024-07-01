def dash(x):
    listHps = sorted(x.split("-"))
    joinHps = "-".join(listHps)
    
    return joinHps

x = input("Enter items with (-): ")
print(f"Sorted items: {dash(x)}")