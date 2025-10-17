import pandas as pd

from solution import add_virtual_column


def main() -> None:
    """
    Main function with simple demo
    """
    fruits_sales = pd.DataFrame([["banana", 10, 10], ["apple", 3, 1]], columns=["name", "quantity", "price"])
    print(fruits_sales)

    sales_total = add_virtual_column(fruits_sales, "quantity * price", "total")
    print(sales_total)


if __name__ == "__main__":
    main()
