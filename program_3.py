total_sales = int(input("Enter the total sales for this month: "))

def county():
    county_sales_tax = total_sales * 0.025
    print(f"Your county sales tax amount is ${county_sales_tax:.2f}.")
    
    return county_sales_tax

def state():
    state_sales_tax = total_sales * 0.05
    print(f"Your state sales tax amount is ${state_sales_tax:.2f}.")

    return state_sales_tax

county_sales_tax = county()
state_sales_tax = state()

total_sales_tax = county_sales_tax + state_sales_tax

print(f"Your total sales tax is ${total_sales_tax:.2f}")