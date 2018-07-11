def use_cte_to_determine_average_sale():
    return """WITH average_sales AS (SELECT AVG(amount) as average_amount from sales) SELECT * FROM average_sales;"""

def select_all_above_average_sales():
    return """
        WITH average_sales AS (SELECT AVG(amount) as average_amount from sales)
         SELECT * FROM sales WHERE sales.amount > (SELECT AVG(amount) from sales);;
    """


"SELECT name FROM customers WHERE customers.id IN (SELECT customer_id from user_events WHERE user_events.login_date > );"


'SELECT *, AVG(amount) as sales_amount FROM sales HAVING sales.amount > sales_amount;'
