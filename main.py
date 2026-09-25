import random
import string
from pyscript import display, document


def handle_order(e):
    name = document.getElementById("customerName").value
    email = document.getElementById("customerEmail").value
    coffee_type = document.querySelector('input[name="coffeeType"]:checked').value
    quantity = document.getElementById("orderQuantity").value
    calculate_price = lambda coffee_type, quantity: {
        "Espresso": 35,
        "Latte": 35,
        "Cappuccino": 40,
        "Americano": 35
    }.get(coffee_type, 0) * int(quantity)
    sku_characters = string.ascii_uppercase + string.digits
    sku_value = "".join(random.choices(sku_characters, k=12))
    sku_number = "-".join(sku_value[index:index + 4] for index in range(0, 12, 4))

    display(f"Name: {name}", target="summaryName", append=False)
    display(f"Email: {email}", target="summaryEmail", append=False)
    display(f"Coffee Ordered:{coffee_type}", target="summaryCoffeeType", append=False)
    display(f"Quantity: {quantity}", target="summaryQuantity", append=False)
    display(
        f"Total Price: ${calculate_price(coffee_type, quantity)}",
        target="summaryTotalPrice",
        append=False,
    )
    display(f"SKU Number: {sku_number}", target="summarySkuNumber", append=False)

def skugen(e):
    document.getElementById("summarySkuNumber").innerHTML = " "

    category = document.getElementById("category").value
    product_name = document.getElementById("productName").value
    stock_qty = document.getElementById("stockQuantity").value

    sku = (
        category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(stock_qty)
    )

    display("SKU: ", sku, target="summarySkuNumber")
    
