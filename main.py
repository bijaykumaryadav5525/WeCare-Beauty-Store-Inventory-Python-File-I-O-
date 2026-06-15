from read import read_products, display_products
from write import write_products, generate_sales_invoice, generate_restock_invoice
from operations import process_sale, process_restock, find_product_by_name

PRODUCTS_FILE = "products.txt"

def main_menu():
    print("\n*** WeCare Store Menu ***")
    print("1. Display Products")
    print("2. Sell ")
    print("3. Buy/Restock")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 4.")

def sell_products(products):
    display_products(products)
    items_purchased = []
    total_amount = 0
    customer_name = input("\nEnter customer name: ")

    while True:
        product_name = input("\nEnter product name to sell (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        product_idx = find_product_by_name(products, product_name)
        if product_idx is None:
            print("Product not found.")
            continue

        try:
            quantity = int(input("Enter quantity to sell: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        products, invoice_item, item_total = process_sale(products, product_idx, quantity, customer_name)

        if invoice_item:
            items_purchased.append(invoice_item)
            total_amount += item_total
            print("\nSold: Buy 3 get 1 free. %d %s (+%d free)" % (quantity, product_name, invoice_item['free']))
            print("Total Price: Rs %.2f" % item_total)

    if items_purchased:
        # Generate and display the invoice
        invoice_text = generate_sales_invoice(customer_name, items_purchased, total_amount, print_to_console=True)
        write_products(PRODUCTS_FILE, products)
        print("\nSale completed successfully!")
    else:
        print("\nNo products were sold.")

def restock_products(products):
    display_products(products)
    items_restocked = []
    total_amount = 0
    supplier_name = input("\nEnter admin name: ")

    while True:
        product_name = input("\nEnter product name to restock (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        product_idx = find_product_by_name(products, product_name)
        if product_idx is None:
            print("Product not found.")
            continue

        try:
            quantity = int(input("Enter quantity to restock: "))
            cost_price = float(input("Enter new cost price: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        products, invoice_item, item_total = process_restock(products, product_idx, quantity, cost_price, supplier_name)

        if invoice_item:
            items_restocked.append(invoice_item)
            total_amount += item_total
            print("\nRestocked: %d %s" % (quantity, product_name))
            print("Total Restock Cost: Rs %.2f" % item_total)

    if items_restocked:
        # Generate and display the restock invoice
        invoice_text = generate_restock_invoice(supplier_name, items_restocked, total_amount, print_to_console=True)
        write_products(PRODUCTS_FILE, products)
        print("\nRestock completed successfully!")
    else:
        print("\nNo products were restocked.")

def main():
    products = read_products(PRODUCTS_FILE)
    while True:
        choice = main_menu()
        if choice == '1':
            display_products(products)
        elif choice == '2':
            sell_products(products)
        elif choice == '3':
            restock_products(products)
        elif choice == '4':
            print("\nThank you! for using the WeCare Skin Care Product System!")
            break

if __name__ == "__main__":
    main()
