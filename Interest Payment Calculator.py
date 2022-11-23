# collect the necessary inputs: principal, apr (annual interest rate), years
# calculate the monthly payment
# show to the user

def main():
    print("This is a monthly payment loan calculator", "\n")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Enter amount of years: "))

    monthly_interest_rate = apr / 1200
    months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))

    print("The monthly payment for this loan will be: %.2f" % monthly_payment)
