'''Calculate income tax for the given income by adhering to the rules below
Taxable Income   	Rate (in %)
First $10,000   	0
Next $10,000	    10
The remaining    	20'''

def income_tax(income):
    tax = 0
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.1
    else:
        tax = 10000 * 0.1 + (income - 20000) * 0.2
    return tax

income = int(input("Enter your income: $"))
tax = income_tax(income)
print(f"Your income tax is ${tax}")