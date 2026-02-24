def calculate_discount(category, tier):
    category_discounts = {
        "Electronics": 10,
        "Clothing": 15,
        "Books": 5,
        "Home": 12
    }

    tier_discounts = {
        "Premium": 5,
        "Standard": 0,
        "Budget": 2
    }

    return category_discounts.get(category, 0) + tier_discounts.get(tier, 0)


def process_products():
    products = []
    total_discount = 0

    try:
        with open("products.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 4:
                    print("Invalid line format, skipping.")
                    continue

                name, price_str, category, tier = parts

                try:
                    price = float(price_str)
                except ValueError:
                    print(f"Invalid price for product {name}, skipping.")
                    continue

                discount_percent = calculate_discount(category, tier)
                discount_amount = price * (discount_percent / 100)
                final_price = price - discount_amount

                products.append((name, price, discount_percent, discount_amount, final_price))
                total_discount += discount_percent

        # Write report
        with open("pricing_report.txt", "w") as report:
            report.write("PRICING REPORT\n")
            report.write("=" * 60 + "\n")
            report.write(f"{'Product':25}{'Base':>10}{'Disc%':>10}{'Final':>10}\n")
            report.write("=" * 60 + "\n")

            for p in products:
                report.write(f"{p[0]:25}{p[1]:>10.2f}{p[2]:>10}{p[4]:>10.2f}\n")

            report.write("=" * 60 + "\n")

        # Console summary
        print("Processing complete.")
        print(f"Total products: {len(products)}")

        if products:
            avg_discount = total_discount / len(products)
            print(f"Average discount applied: {avg_discount:.2f}%")

    except FileNotFoundError:
        print("Error: products.txt file not found.")
    except PermissionError:
        print("Error: Permission denied.")


if __name__ == "__main__":
    process_products()