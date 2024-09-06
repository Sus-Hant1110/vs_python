# program that calculates price of a product after discount
# discount is in percentage

def calculate_price(price, discount):
    return price - (price * discount / 100)

price = float(input("Enter price of product: "))
discount = float(input("Enter discount percentage: "))
print("Price after discount: ", calculate_price(price, discount))

