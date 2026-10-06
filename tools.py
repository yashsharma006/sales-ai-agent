from langchain_core.tools import tool
from database import run_query


@tool
def get_sales_by_date(date):
    """Get total sales for a specific date. Date format: YYYY-MM-DD."""

    result = run_query(
        """
        SELECT SUM(total)
        FROM sales
        WHERE sale_date = %s
        """,
        (date,)
    )

    return float(result[0][0] or 0)


@tool
def get_sales_by_date_range(start_date, end_date):
    """Get total sales between two dates. Dates format: YYYY-MM-DD."""

    result = run_query(
        """
        SELECT SUM(total)
        FROM sales
        WHERE sale_date BETWEEN %s AND %s
        """,
        (start_date, end_date)
    )

    return float(result[0][0] or 0)


@tool
def compare_today_yesterday():
    """Compare today's sales with yesterday's sales."""

    result = run_query(
        """
        SELECT
            SUM(CASE WHEN sale_date = CURDATE() THEN total ELSE 0 END),
            SUM(CASE WHEN sale_date = DATE_SUB(CURDATE(), INTERVAL 1 DAY)
                     THEN total ELSE 0 END)
        FROM sales
        """
    )

    today = float(result[0][0] or 0)
    yesterday = float(result[0][1] or 0)

    difference = today - yesterday

    return {
        "today": today,
        "yesterday": yesterday,
        "difference": difference
    }

@tool
def get_product_sales(product):
    """Get total quantity and revenue for a specific product."""

    result = run_query(
        """
        SELECT SUM(quantity), SUM(total)
        FROM sales
        WHERE product = %s
        """,
        (product,)
    )

    quantity = result[0][0] or 0
    revenue = result[0][1] or 0

    return {
        "product": product,
        "quantity_sold": quantity,
        "revenue": float(revenue)
    }


@tool
def get_best_selling_product():
    """Get the product with the highest total quantity sold."""

    result = run_query(
        """
        SELECT product, SUM(quantity) AS quantity
        FROM sales
        GROUP BY product
        ORDER BY quantity DESC
        LIMIT 1
        """
    )

    if not result:
        return "No sales found."

    return {
        "product": result[0][0],
        "quantity_sold": result[0][1]
    }


@tool
def get_highest_revenue_product():
    """Get the product that generated the highest revenue."""

    result = run_query(
        """
        SELECT product, SUM(total) AS revenue
        FROM sales
        GROUP BY product
        ORDER BY revenue DESC
        LIMIT 1
        """
    )

    if not result:
        return "No sales found."

    return {
        "product": result[0][0],
        "revenue": float(result[0][1])
    }

tools = [
    get_sales_by_date,
    get_sales_by_date_range,
    compare_today_yesterday,
    get_product_sales,
    get_best_selling_product,
    get_highest_revenue_product
]

# print(get_best_selling_product.invoke({})) 