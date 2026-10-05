from pyscript import display, document


def SKU_generator(e):
    # Clears the previous output container
    document.getElementById('sku_output').innerHTML = " "
   
    # Retrieves input values from the HTML fields
    category = document.getElementById('category').value
    product_name = document.getElementById('prod_name').value
    stock_qty = document.getElementById('quantity').value
   
    # Generates the unique SKU code
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
   
    # Renders the result to the page
    display("SKU: " + sku, target='sku_output')


def create_order(e):
    # Get input values
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
   
    # Calculate total by multiplying value by checked status (1 or 0)
    subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked +
                float(prod4.value) * prod4.checked +
                float(prod5.value) * prod5.checked)
   
    tax_rate = 0.12 # 12% VAT
    tax = subtotal * tax_rate
    total = subtotal + tax
   
    receipt = f"""
    <center><h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT: ₱{tax:.2f}</p>
    <h3><strong>Total: ₱{total:.2f}</strong></p></center>
    """
   
    # FIX: Use display with append=False instead of innerHTML
    display(receipt, target="show", append=False)
   
    # Updates the target element with HTML formatting
    document.getElementById("show").innerHTML = receipt
