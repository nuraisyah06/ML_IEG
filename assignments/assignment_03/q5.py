total = float(input("Total investment: RM "))
rateA = float(input("Interest rate account A: ")) / 100
rateB = float(input("Interest rate account B: ")) / 100
profit = float(input("Total profit: RM "))

MA = (profit-total*rateB)/(rateA-rateB)
MB = total - MA

print(f"Money invested in Account A: RM{MA:.2f}")
print(f"Money invested in Account B: RM{MB:.2f}")

