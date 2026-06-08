def main():
    print("Car Savings Goal Calculator")
    target_amount = float(input("Enter the target downpayment amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    r = annual_interest_rate / 100
    k = 12
    monthly_rate = r / k
    multiplier = (((1 + monthly_rate) ** 24) - 1) / monthly_rate
    d = target_amount / multiplier
    print("To reach your goal, you need to deposit:", d)

main()