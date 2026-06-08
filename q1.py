
import math
def main():
    print("Compound interest calculator")
    initial_investment = float(input("Enter the initial investment: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the number of years: "))
    r = annual_interest_rate / 100
    final_amount = initial_investment * math.exp(r * years)
    print(f"The final amount after {years} years is: {final_amount:.2f}")
main()