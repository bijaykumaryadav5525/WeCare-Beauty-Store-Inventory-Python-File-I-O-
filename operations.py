''' functions process_sale for transaction and returns update a list
    parameters:
    products(list)
    products_index(int)
    quantity(int)
    customer_name(str)'''
def process_sale(products, product_index, quantity, customer_name):
    """
    Processes a sale transaction and returns updated products and invoice items.
    Implements 'buy 2 get 1 free' policy.
    """
    #checked the products selection is valid or not
    if product_index < 0 or product_index >= len(products):
        print("Invalid product selection.")
        return products, None, 0

    product = products[product_index]
    #checked valid for quantity
    if quantity <= 0:
        print("Quantity must be positive.")
        return products, None, 0
    #checked stock abilability
    if product['quantity'] < quantity:
        print(f"Not enough stock. Only {product['quantity']} available.")
        return products, None, 0

    # Calculating offers items (buy 3 get 1 free)
    free_items = quantity // 3
    total_items = quantity + free_items

    # Update stock
    products[product_index]['quantity'] -= quantity

    # Calculate total price (customer pays only for purchased items, not free ones)
    selling_price = calculate_selling_price(product['cost_price'])
    total_price = quantity * selling_price

    # Prepare invoice item
    invoice_item = {
        'name': product['name'],
        'brand': product['brand'],
        'quantity': quantity,
        'free': free_items,
        'unit_price': selling_price,
        'total_price': total_price
    }

    return products, invoice_item, total_price
''' functions Updates stock levels by restocking existing products and prepares restock invoice data.
    
    Parameters:
    - products (list)
    - product_index (int) 
    - quantity (int).
    - cost_price (float): New cost price per unit.
    - supplier_name (str):'''
def process_restock(products, product_index, quantity, cost_price, supplier_name):
    """Processes a restock transaction and returns updated products and invoice items."""
    if product_index < 0 or product_index >= len(products):
        print("Invalid product selection.")
        return products, None, 0

    if quantity <= 0:
        print("Quantity must be positive.")
        return products, None, 0

    if cost_price <= 0:
        print("Cost price must be positive.")
        return products, None, 0

    product = products[product_index]

    # Update product quantity and cost price
    products[product_index]['quantity'] += quantity
    products[product_index]['cost_price'] = cost_price

    # Calculate total cost
    total_cost = quantity * cost_price

    # Prepare invoice item
    invoice_item = {
        'name': product['name'],
        'brand': product['brand'],
        'quantity': quantity,
        'cost_price': cost_price,
        'total_price': total_cost
    }

    return products, invoice_item, total_cost


''' functions  Searches for a product by name (case-insensitive) and returns its index.
    
    Parameters:
    - products (list): List of product dictionaries.
    - name (str): find products.
    
    Returns:
      index (int) if found, else None''' 
def find_product_by_name(products, name):
    """Finds a product by name (case-insensitive) and returns its index or None."""
    for idx, product in enumerate(products):
        if product['name'].lower() == name.lower():
            return idx
    return None

def calculate_selling_price(cost_price):
    """Calculates selling price with 200% markup."""
    return cost_price * 2  # Changed from 2 to 3 for 200% markup (cost * (1 + 2))
