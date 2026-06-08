def main():
    print("Car Savings Calculator")
    d = 100
    annual_interest_rate = 3.0
    r = annual_interest_rate / 100
    k = 12
    monthly_rate = r / k
    final_amount = d * (((1 + monthly_rate) ** 24) - 1) / monthly_rate
    print("The final amount after 2 years is:", final_amount)

main()