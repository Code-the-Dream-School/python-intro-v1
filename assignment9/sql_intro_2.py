import sqlite3
import pandas as pd

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        sql_statement = """
        SELECT line_items.line_item_id,
               line_items.quantity,
               line_items.product_id,
               products.product_name,
               products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        """

        df = pd.read_sql_query(sql_statement, conn)

        print(df.head())

        df["total"] = df["quantity"] * df["price"]

        print(df.head())
        summary_df = df.groupby("product_id").agg(
        line_item_count=("line_item_id", "count"),
        total_paid=("total", "sum"),
        product_name=("product_name", "first")
)

    print(summary_df.head())

    summary_df = summary_df.sort_values("product_name")

    summary_df.to_csv("order_summary.csv")

    print(summary_df.head())

except sqlite3.Error as e:
    print("Database error:", e)



