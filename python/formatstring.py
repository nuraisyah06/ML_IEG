name = "David"
batch = 101
fee = 134.7654
# traditionally how we do this
inputstring = "Hello" + name + ", welcome to python class" + str(batch)
print(inputstring)

#special string called f stirng
inputstring = f"Hello {name} , welcome to python class {batch}" 
print(inputstring)

#special string called f stirng// it have 40 character space
inputstring = f"Hello {name:40s} , welcome to python class {batch}" 
print(inputstring)

#align David to center
inputstring = f"Hello {name:^40s} , welcome to python class {batch}" 
print(inputstring)

#align David to right
inputstring = f"Hello {name:>40s} , welcome to python class {batch}" 
print(inputstring)

#provide padding  characters
inputstring = f"Hello {name:*>40s} , welcome to python class {batch}" 
print(inputstring)

#trucate to 3 characters
inputstring = f"Hello {name:.3} , welcome to python class {batch}" 
print(inputstring)

#focs on decimal let us take 10 space
inputstring = f"Hello {name:.3} , welcome to python class {batch:10d} in KL" 
print(inputstring)

#focs on decimal let us take 10 space
inputstring = f"Hello {name:.3} , welcome to python class {batch:<10d} in KL" 
print(inputstring)

#focs on decimal let us take 10 space
inputstring = f"Hello {name:.3} , welcome to python class {batch:<10d} in KL for RM {fee:10.2f}" 
print(inputstring)

#binary
inputstring = f"Hello {name:.3} , welcome to python class {batch:b} in KL for RM {fee:.2f}" 
print(inputstring)

#octal
inputstring = f"Hello {name:.3} , welcome to python class {batch:o} in KL for RM {fee:10.2f}" 
print(inputstring)

#octal
inputstring = f"Hello {name:.3} , welcome to python class {batch:x} in KL for RM {fee:10.2f}" 
print(inputstring)

#octal
inputstring = f"Hello {name:.3} , welcome to python class {batch:x} in KL for RM {fee:,.2f}" 
print(inputstring)