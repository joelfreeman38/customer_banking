# Import the Account class from the Account.py file.
from savings_account import create_savings_account  # Assuming the function is defined in savings_account.py
from cd_account import create_cd_account  # Assuming the function is defined in cd_account.py

# Main function to handle user input and display results
def main():
    """Prompts the user for savings account details and calculates interest and updated balance."""
    try:
        # Get user input for savings account
        balance = float(input("Enter the savings account balance: $"))
        interest_rate = float(input("Enter the savings account interest rate (APR in %): "))
        months = int(input("Enter the number of months for savings account: "))

        # Call the create_savings_account function
        updated_balance, interest_earned = create_savings_account(balance, interest_rate, months)

        # Print out the interest earned and updated savings account balance with interest earned for the given months.
        print(f"Savings1 Account - Interest Earned: ${interest_earned:.2f}")
        print(f"Savings Account - Updated Balance: ${updated_balance:.2f}")

# Get user input for cd account
        balance = float(input("Enter the cd account balance: $"))
        interest_rate = float(input("Enter the cd account interest rate (APR in %): "))
        months = int(input("Enter the number of months for cd account: "))

        # Call the create_savings_account function
        updated_balance, interest_earned = create_cd_account(balance, interest_rate, months)

        # Print out the interest earned and updated cd account balance with interest earned for the given months.
        print(f"cd account - Interest Earned: ${interest_earned:.2f}")
        print(f"cd account - Updated Balance: ${updated_balance:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for balance, interest rate, and months.")

# Call the main function
if __name__ == "__main__":
    main()
