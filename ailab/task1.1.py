def discount(price, category):
    return price * (0.9 if category == "student" and price > 1000 else
                    0.95 if category == "student" else
                    0.85 if price > 2000 else 1)

total_price = 1000 + 1500
print("Total Price:", total_price)
print("Discounted Price:", discount(total_price, "student"))
