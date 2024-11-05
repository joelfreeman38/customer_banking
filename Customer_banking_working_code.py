# Import the Account class from the Account.py file.
from Account import Account

# Define the function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: The updated savings account balance after adding the interest earned, and the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings_account = Account(balance, 0)  # Interest is initialized as 0

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set_balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set_interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned


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
        print(f"Savings Account - Interest Earned: ${interest_earned:.2f}")
        print(f"Savings Account - Updated Balance: ${updated_balance:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for balance, interest rate, and months.")

# Call the main function
if __name__ == "__main__":
    main()
