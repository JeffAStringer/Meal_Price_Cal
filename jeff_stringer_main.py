child_meal = float(4.50)
adult_meal = float(9.00)
shake_drink = float(1.75)
Pie_dessert = float(1.00)

child = (int(input ( "How adults are eating today? " ))) 
adult = (int(input( "How many children are eating today? ")))
shake = (int(input(  "How many icecream shakes do you want to drink? ")))
pie = (int(input ( "How many cherry pies would you like? ")))
sales_tax = float(0.06)


subtotal = ((child_meal * child) + (adult_meal * adult) + (shake_drink * shake) + (Pie_dessert * pie))
subtotal_formatted = "{:.2f}".format(subtotal)
my_str = (str(" Subtotal "))
print(f"{my_str} ${subtotal_formatted}")
# print (f"${subtotal}")

sales_tax = (((child_meal * child)+(adult_meal * adult) + (shake_drink * shake) + (Pie_dessert * pie) * sales_tax))
sales_tax_formatted = "{:.2f}".format(sales_tax)
sales_tax_print = (str(" Sales Tax "))
print(f"{sales_tax_print} ${sales_tax_formatted}")
# print(f"${sales_tax}")

total_sale = sales_tax + subtotal
total_sale_formatted = "{:.2f}".format(total_sale)
total_sale_print = (str(" Total Sale "))
print(f"{total_sale_print} ${total_sale_formatted}")
# print(f"${total_sale}")

Amount_paid = float(input(" How much will you be paying? $"))
Amount_paid_float = float(Amount_paid)
Change = (float(total_sale_formatted) - (Amount_paid_float))
Change_formatted = "{:.2f}".format(Change)
print(f" ${Change_formatted}")
