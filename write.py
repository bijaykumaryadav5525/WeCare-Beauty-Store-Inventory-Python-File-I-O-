#import datetime on write.py files
import datetime

def write_products(file_path, products):
    """Writes product data back to the text file.
       parameters:
       file_path and products
       products  acts list for dictionaries with keys:name,brand,quantity,cost price and country
       """
    try:
        with open(file_path, 'w') as file:
            for product in products:
                line = "%s, %s, %d, %.2f, %s\n" % (
                    product['name'],
                    product['brand'],
                    product['quantity'],
                    product['cost_price'],
                    product['country']
                )
                file.write(line)
    except Exception as e: # when file not reads that times print exception
        print("An error occurred while writing to the file: %s" % e)
'''functions generate_sales_invoice as a text file.
    Parameters:
    customer name(str)
    items_purchased(list)
    total_amount(float)
    print_to_console(boolean)'''

def generate_sales_invoice(customer_name, items_purchased, total_amount, print_to_console=False):
    """Generates a sales invoice text file for a customer and optionally prints to console."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sales_invoice_{timestamp}.txt"  # Removed directory reference
    invoice_content = []

    invoice_content.append("=== SALES INVOICE ===")
    invoice_content.append("Date: %s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    invoice_content.append("Customer: %s" % customer_name)
    invoice_content.append("-" * 80)
    invoice_content.append("%-20s%-15s%-5s%-5s%-10s" % ('Product', 'Brand', 'Qty', 'Free', 'Price'))
    invoice_content.append("-" * 80)
    # add all purchased item to the invoice
    for item in items_purchased:
        invoice_content.append("%-20s%-15s%-5d%-5d%-10.2f" % (
            item['name'],
            item['brand'],
            item['quantity'],
            item['free'],
            item['total_price']
        ))

    invoice_content.append("-" * 80)
    invoice_content.append("TOTAL AMOUNT: Rs %.2f" % total_amount)
    invoice_content.append("=" * 80)
    #save all details to the invoice to a text files
    try:
        with open(filename, 'w') as file:
            file.write("\n".join(invoice_content))
        print("\nSales invoice generated: %s" % filename)
    except Exception as e:
        print("Error generating sales invoice: %s" % e)

    invoice_text = "\n".join(invoice_content)

    if print_to_console:
        print("\n=== BILL ===")
        print(invoice_text)

    return invoice_text
''' functions generate_restock_invoice as a text file for a supplier.
    Parameters:
    supplier_name(str)
    items_restock(list)
    total_amount(float)
    print_to_console(boolean)'''
def generate_restock_invoice(supplier_name, items_restocked, total_amount, print_to_console=False):
    """Generates a restock invoice text file for a supplier and optionally prints to console."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"restock_invoice_{timestamp}.txt"  # Removed directory reference
    invoice_content = []

    invoice_content.append("=== RESTOCK INVOICE ===")
    invoice_content.append("Date: %s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    invoice_content.append("Supplier: %s" % supplier_name)
    invoice_content.append("-" * 80)
    invoice_content.append("%-20s%-15s%-5s%-10s%-10s" % ('Product', 'Brand', 'Qty', 'Unit Price', 'Total'))
    invoice_content.append("-" * 80)

    for item in items_restocked:
        invoice_content.append("%-20s%-15s%-5d%-10.2f%-10.2f" % (
            item['name'],
            item['brand'],
            item['quantity'],
            item['cost_price'],
            item['total_price']
        ))

    invoice_content.append("-" * 80)
    invoice_content.append("TOTAL AMOUNT: Rs %.2f" % total_amount)
    invoice_content.append("=" * 80)

    try:
        with open(filename, 'w') as file:
            file.write("\n".join(invoice_content))
        print("\nRestock invoice generated: %s" % filename)
    except Exception as e:
        print("Error generating restock invoice: %s" % e)

    invoice_text = "\n".join(invoice_content)

    if print_to_console:
        print("\n=== RESTOCK BILL ===")
        print(invoice_text)

    return invoice_text
