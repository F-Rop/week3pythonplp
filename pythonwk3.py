def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Assumption: Original price fixed at ksh 500
original_price = 500
discount_percent = float(input("Enter the discount percentage: "))

# printing the final price
final_price = calculate_discount(original_price, discount_percent)
print("Final price after discount:", final_price)