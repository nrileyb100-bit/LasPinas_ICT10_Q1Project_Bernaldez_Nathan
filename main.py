from pyscript import display, document, html

def SKU_generator(e):
    category_el = document.getElementById('Category')
    prod_name_el = document.getElementById('prod_name')
    quantity_el = document.getElementById('quantity')
    
    if not category_el or not prod_name_el or not quantity_el:
        return

    output_container = document.getElementById('sku_output')
    if output_container:
        output_container.innerHTML = " "
   
    category = category_el.value
    product_name = prod_name_el.value
    stock_qty = quantity_el.value

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
   
    display("SKU: " + sku, target='sku_output')


def create_order(e):
    items = [
        document.getElementById("item1"),
        document.getElementById("item2"),
        document.getElementById("item3"),
        document.getElementById("item4"),
        document.getElementById("item5")
    ]
    
    if any(item is None for item in items):
        return
   
    subtotal = 0.0
    for item in items:
        if item.checked:
            subtotal += float(item.value)
   
    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax
   
    receipt = f"""
    <center><h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT: ₱{tax:.2f}</p>
    <h3><strong>Total: ₱{total:.2f}</strong></h3></center>
    """

    display(html(receipt), target="show", append=False)



    
