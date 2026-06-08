import math
def main():
    print("Mortgage Monthly Payment Calculator")
    p0 = float(input("Enter the amount to borrow: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the term of the loan in years: ")) 
    r = annual_interest_rate / 100
    k = 12
    d = p0 / ((1 - (1 + r/k)**(-years * k)) / (r/k))
    
    print("Your monthly payment is:", d)

main()