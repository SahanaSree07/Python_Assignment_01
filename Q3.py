
# Q3 - Online Shopping Discount Eligibility

# Accept order amount and membership status
order_amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").strip().lower()

# Validate order amount
if order_amount < 0 or order_amount > 100000:
    print("Invalid Order Amount!")
    
elif membership != "yes" and membership != "no":
    print("Invalid Membership Status! Enter yes or no.")

else:
    # Initialize discount
    discount_percentage = 0

    # Check discount eligibility
    if order_amount >= 5000:
        discount_percentage = 15

    elif order_amount >= 2000 and order_amount < 5000 and membership == "yes":
        discount_percentage = 10

    else:
        discount_percentage = 0

    # Calculate discount and final amount
    discount_amount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount_amount

    # Display results
    print("\n----- Shopping Bill -----")
    print("Original Amount: ₹", order_amount)
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount: ₹", discount_amount)
    print("Final Payable Amount: ₹", final_amount)

    if discount_percentage > 0:
        print("Eligibility Status: Eligible for discount")
    else:
        print("Eligibility Status: Not eligible for discount")
