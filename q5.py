import math

def main():
    print("House Affordability Calculator")
    monthly_payment = float(input("Enter the affordable monthly payment: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    r = annual_interest_rate / 100
    k = 12
    years15 = 15
    final_amount15 = monthly_payment * ((1 - (1 + r/k)**(-years15 * k)) / (r/k))
    years30 = 30
    final_amount30 = monthly_payment * ((1 - (1 + r/k)**(-years30 * k)) / (r/k))
    print("With a 15-year mortgage, you can borrow:", final_amount15)
    print("With a 30-year mortgage, you can borrow:", final_amount30)

main()