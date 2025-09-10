def discount(price, category):
    if category == "student":
        if price > 1000:
            return price * 0.9
        else:
            return price * 0.95
    else:
        if price > 2000:
            return price * 0.85
        else:
            return price

def add(price1, price2):
    return price1 + price2
total_price = add(1000, 1500)
print("Total Price:", total_price)
discounted_price = discount(total_price, "student")
print("Discounted Price:", discounted_price)



