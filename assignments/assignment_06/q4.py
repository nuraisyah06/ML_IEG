def product_of_digits(number):
    number_str = str(number)
    
    product = 1
    
    for digit in number_str:
        product *= int(digit)
    
    return product

num = int(input("Enter a number: "))
print(f"The product of the digits of {num} is {product_of_digits(num)}")
