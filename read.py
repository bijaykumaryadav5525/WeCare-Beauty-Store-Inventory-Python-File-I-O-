def read_products(file_path):
    """
    Reads product data from a text file and returns it as a list of dictionaries.
    Each product is represented as a dictionary with keys: name, brand, quantity, cost_price, country.
    """
    products = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line:
                    continue  # Skip empty lines

                parts = line.split(',')

                # Ensure we have all 5 parts
                if len(parts) == 5:
                    product = {
                        'name': parts[0],
                        'brand': parts[1],
                        'quantity': int(parts[2]),
                        'cost_price': float(parts[3]),
                        'country': parts[4]
                    }
                    products.append(product)
    except FileNotFoundError:
        print("Error: The file %s was not found." % file_path)
    except Exception as e:
        print("An error occurred while reading the file: %s" % e)

    return products


def display_products(products):
    """Displays product information in a readable format."""
    if not products:
        print("No products available.")
        return

    print("\nAvailable Products:")
    print("-" * 80)
    print("%-5s%-20s%-15s%-10s%-15s%-15s" % ('No.', 'Product Name', 'Brand', 'Qty', 'Price (Rs)', 'Country'))
    print("-" * 80)

    for idx, product in enumerate(products, 1):
        selling_price = product['cost_price'] * 2  # 200% markup
        print("%-5d%-20s%-15s%-10d%-15.2f%-15s" % (
            idx,
            product['name'],
            product['brand'],
            product['quantity'],
            selling_price,
            product['country']
        ))
    print("-" * 80)
