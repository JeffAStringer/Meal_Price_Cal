child_meal = float(4.50)
adult_meal = float(9.00)
child = (int(input ( "How adults are eating today? " ))) 
adult = (int(input( "How many children are eating today? ")))
sales_tax = float(0.06)

subtotal = ((child_meal * child) + (adult_meal * adult))
subtotal_formatted = "{:.2f}".format(subtotal)
print(f"${subtotal_formatted}")
# print (f"${subtotal}")

sales_tax = (((child_meal * child)+(adult_meal * adult))* sales_tax)
sales_tax_formatted = "{:.2f}".format(sales_tax)
print(f"${sales_tax_formatted}")
# print(f"${sales_tax}")

total_sale = sales_tax + subtotal
total_sale_formatted = "{:.2f}".format(total_sale)
print(f"${total_sale_formatted}")
# print(f"${total_sale}")

