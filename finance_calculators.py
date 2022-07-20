import math

# Main selection - bond or investment
print("""Choose either 'investment' or 'bond' from the menu below in order to proceed: 
investment \t - to calculate the amount of interest you'll earn on interest
bond \t\t - to calculate the amount you'll have to pay on a home loan
: """ )

# Get user's input and convert it to uppercase in order to ensure the if choice works correctly
choice = input().upper()

# Validate the user's choice
if choice not in ['BOND', 'INVESTMENT']:    # This "not in" I got from
                                            # https://blogs.glowscotland.org.uk/sh/ahscomputingpython/national-5/input-validation/
                                            # I tried "if choice != ("BOND" or "INVESTMENT") and it didn't work, as well as
                                            # without the brackets. So I am unsure as to why it didn't work
    print("Please enter either 'bond' or 'investment'.")

# INVESTMENT
if choice == "INVESTMENT":
    amount_depositing = float(input("How much money are you depositing? "))
    interest_rate = float(input("What is the interest rate? "))
    years_investing = float(input("How long will you be investing your money? "))
    interest = input("Do you want 'simple' or 'compound' interest? ").upper()

    if interest == "SIMPLE":
        simple_interest_calculation = amount_depositing * (1 + interest_rate / 100 * years_investing)
        print("R{}.".format(simple_interest_calculation))
    if interest == "COMPOUND":
        compound_interest_calculation = amount_depositing * math.pow((1+interest_rate / 100))
        print("R{}.".format(compound_interest_calculation))

# BOND REPAYMENT
if choice == "BOND":
    present_value_of_house = float(input("What is the current value of your house? "))
    interest_rate = float(input("What is the interest rate? "))
    number_of_months_to_repay = float(input("How many months do you plan on repaying the house? "))
    bond_payment =round(((interest_rate / 100 / 12) * present_value_of_house) / (1 - (1 + interest_rate / 100) ** (- number_of_months_to_repay)), 2)
    print("R{}.".format(bond_payment))
