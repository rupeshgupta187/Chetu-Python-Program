total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]


  
for x, y in zip(total_sales,prod_cost,):
        profit=x-y
        print(f'{total_sales.index(x)}--> profit is :{profit}')
