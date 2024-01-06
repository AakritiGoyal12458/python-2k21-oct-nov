import pandas as pd 
import matplotlib.pyplot as plt

#import time
plt.figure(figsize=(15,7))
img = plt.imread(r"D\IMAGES\furniture.jpg")
plt.figure(figsize=(9,9))
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
print("#"*100)
print('''
    ██     ██ ███████ ██       ██████  ██████  ███    ███ ███████           
    ██     ██ ██      ██      ██      ██    ██ ████  ████ ██                
    ██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████             
    ██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██                
     ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████           
                                                                            
                                                                            
        ████████  ██████       ██████  ██    ██ ██████                      
           ██    ██    ██     ██    ██ ██    ██ ██   ██                     
           ██    ██    ██     ██    ██ ██    ██ ██████                      
           ██    ██    ██     ██    ██ ██    ██ ██   ██                     
           ██     ██████       ██████   ██████  ██   ██                     
                                                                            
                                                                            
███████ ██    ██ ██████  ███    ██ ██ ████████ ██    ██ ██████  ███████     
██      ██    ██ ██   ██ ████   ██ ██    ██    ██    ██ ██   ██ ██          
█████   ██    ██ ██████  ██ ██  ██ ██    ██    ██    ██ ██████  █████       
██      ██    ██ ██   ██ ██  ██ ██ ██    ██    ██    ██ ██   ██ ██          
██       ██████  ██   ██ ██   ████ ██    ██     ██████  ██   ██ ███████     
                                                                            
                                                                            
███████ ██   ██  ██████  ██     ██ ██████   ██████   ██████  ███    ███     
██      ██   ██ ██    ██ ██     ██ ██   ██ ██    ██ ██    ██ ████  ████     
███████ ███████ ██    ██ ██  █  ██ ██████  ██    ██ ██    ██ ██ ████ ██     
     ██ ██   ██ ██    ██ ██ ███ ██ ██   ██ ██    ██ ██    ██ ██  ██  ██     
███████ ██   ██  ██████   ███ ███  ██   ██  ██████   ██████  ██      ██                                                               
''')
print("#"*100)
while True:
    try:
        print("Enter the file no")
        print("1. Emp file")
        print("2. Customer file")
        print("3. Product file")
        print("4. Supplier file")
        print("-1. Stop the app")
        
        file_number = int(input("Enter file no: "))
        
        if file_number == 1:
            employee_df = pd.read_csv("D\Class12CA\Emp.csv")
            while True:
                print("Enter the operation no")
                print("1. Add a row")
                print("2. Delete a row")
                print("3. Add a column")
                print("4. Delete a column")
                print("5. View Employee Details")
                print("6. Search Employee")
                print("7. Update Employee Salary")
                print("8. View Employees by Job")
                print("9. Create Line Graph")
                print("10. Create Bar Graph")
                print("11. Create Pie Chart")
                print("12. Analyze data by grouping it based on a specific column")
                print("13. Sort the data based on a chosen column in ascending or descending order")
                print("14. Filter the data based on a specific condition and column")
                print("15. Visualize the distribution of a numeric column using a histogram")
                print("-1. Close Emp file")

                operation = int(input("Enter op no"))

                if operation == 1:
                    
                    emp_no = input("Enter Employee Number: ")
                    emp_name = input("Enter Employee Name: ")
                    job = input("Enter Job Title: ")
                    salary = input("Enter Salary: ")

                    new_row = {'EmpNo': int(emp_no), 'EmpName': emp_name, 'Job': job, 'Salary': int(salary)}
                    employee_df = employee_df.append(new_row, ignore_index=True)
                    employee_df.to_csv("D\Class12CA\Emp.csv", index=False)
                    print("Row is added.")

                elif operation == 2:
                    # Delete a row
                
                    emp_no_to_delete = input("Enter Employee Number to delete: ")
                    employee_df = employee_df[employee_df['EmpNo'] != int(emp_no_to_delete)]
                    employee_df.to_csv("D\Class12CA\Emp.csv", index=False)
                    print("Row is deleted.")

                elif operation == 3:
                    # Add a column
                    
                    column_name = input("Enter Column Name: ")
                    default_value = input("Enter Default Value for the new column: ")
                    employee_df[column_name] = default_value
                    employee_df.to_csv("D\Class12CA\Emp.csv", index=False)
                    print("Column is added.")

                elif operation == 4:
                    # Delete a column
                    
                    column_to_delete = input("Enter Column Name to delete: ")
                    employee_df = employee_df.drop(columns=[column_to_delete])
                    employee_df.to_csv("D\Class12CA\Emp.csv", index=False)
                    print("Column is deleted.")

                elif operation == 5:
                    # View Employee Details
                    employee_df = pd.read_csv("D\Class12CA\Emp.csv")
                    print(employee_df)

                elif operation == 6:
                    # Search Employee
                    
                    search_term = input("Enter Employee Number or Name to search: ")
                    result = employee_df[
                        (employee_df['EmpNo'] == int(search_term)) | (employee_df['EmpName'].str.contains(search_term, case=False))
                    ]
                    print(result)

                elif operation == 7:
                    # Update Employee Salary
                   
                    emp_no_to_update = input("Enter Employee Number to update salary: ")
                    new_salary = input("Enter the new salary: ")
                    employee_df.loc[employee_df['EmpNo'] == int(emp_no_to_update), 'Salary'] = new_salary
                    employee_df.to_csv("D\Class12CA\Emp.csv", index=False)
                    print("Salary is updated.")

                elif operation == 8:
                    # View Employees by Job
                    
                    job_to_view = input("Enter Job Title to view employees: ")
                    result = employee_df[employee_df['Job'] == job_to_view]
                    print(result)
                elif operation == 9:
                    # Create Line Graph
                    employee_df.plot(x='EmpNo', y='Salary', kind='line')
                    plt.title('Line Graph of Employee Salaries')
                    plt.xlabel('Employee Number')
                    plt.ylabel('Salary')
                    plt.show()

                elif operation == 10:
                    # Create Bar Graph
                    employee_df.plot(x='EmpNo', y='Salary', kind='bar')
                    plt.title('Bar Graph of Employee Salaries')
                    plt.xlabel('Employee Number')
                    plt.ylabel('Salary')
                    plt.show()

                elif operation == 11:
                    # Create Pie Chart
                    plt.pie(employee_df['Salary'], labels=employee_df['EmpNo'], autopct='%1.1f%%')
                    plt.title('Pie Chart of Employee Salaries')
                    plt.show()
                
                elif operation == 12:
                    # Group By
                    group_by_column = input("Enter column name to group by: ")
                    grouped_data = employee_df.groupby(group_by_column).size().reset_index(name='Count')
                    print(grouped_data)

                elif operation == 13:
                    # Sorting
                    sort_by_column = input("Enter column name to sort by: ")
                    ascending_order = input("Sort in ascending order? (yes/no): ").lower() == 'yes'
                    employee_df = employee_df.sort_values(by=sort_by_column, ascending=ascending_order)
                    print("Data after sorting:")
                    print(employee_df)

                elif operation == 14:
                    # Filtering
                    filter_column = input("Enter column name to filter by: ")
                    filter_value = input("Enter value to filter by: ")
                    filtered_data = employee_df[employee_df[filter_column] == filter_value]
                    print(filtered_data)

                elif operation == 15:
                    # Histogram
                    histogram_column = input("Enter column name for histogram: ")
                    employee_df[histogram_column].hist()
                    plt.title(f'Histogram of {histogram_column}')
                    plt.xlabel(histogram_column)
                    plt.ylabel('Frequency')
                    plt.show()


                elif operation == -1:
                    print("Emp file is closed.")
                    break

                else:
                    print("Invalid operation. Please enter a valid option.")
        elif file_number == 2:
            customer_df = pd.read_csv("D\Class12CA\Customer.csv")
            pd.set_option('display.max_columns', None)

            while True:
                print("Enter the operation no")
                print("1. Add a row")
                print("2. Delete a row")
                print("3. Add a column")
                print("4. Delete a column")
                print("5. View Customer Details")
                print("6. Search Customer")
                print("7. Update Customer Email")
                print("8. View Customers by Payment Mode")
                print("9. Create Line Graph")
                print("10. Create Bar Graph")
                print("11. Create Pie Chart")
                print("12. Analyze data by grouping it based on a specific column")
                print("13. Sort the data based on a chosen column in ascending or descending order")
                print("14. Filter the data based on a specific condition and column")
                print("15. Visualize the distribution of a numeric column using a histogram")
                print("-1. Close Customer file")

                operation_customer = int(input("Enter op no"))

                if operation_customer == 1:
                    # Add a row
                    cust_no = input("Enter Customer Number: ")
                    cust_name = input("Enter Customer Name: ")
                    cust_address = input("Enter Customer Address: ")
                    cust_mobile = input("Enter Customer Mobile Number: ")
                    cust_mail = input("Enter Customer Email: ")
                    mode_of_payment = input("Enter Mode of Payment: ")


                    new_row = {'Cust_no': cust_no, 'Cust_name': cust_name, 'Cust_address': cust_address,
                               'Cust_mobile': cust_mobile, 'Cust_mail': cust_mail, 'Mode_of_payment': mode_of_payment}
                    customer_df = customer_df.append(new_row, ignore_index=True)
                    customer_df.to_csv("D\Class12CA\Customer.csv", index=False)
                    print("Customer added successfully.")

                elif operation_customer == 2:
                    # Delete a row
                    cust_no_to_delete = input("Enter Customer Number to delete: ")
                    customer_df = customer_df[customer_df['Cust_no'] != int(cust_no_to_delete)]
                    customer_df.to_csv("D\Class12CA\Customer.csv", index=False)
                    print("Customer is deleted.")

                elif operation_customer == 3:
                    # Add a column
                    column_name = input("Enter Column Name: ")
                    default_value = input("Enter Default Value for the new column: ")
                    customer_df[column_name] = default_value
                    customer_df.to_csv("D\Class12CA\Customer.csv", index=False)
                    print("Column is added.")

                elif operation_customer == 4:
                    # Delete a column
                    column_to_delete = input("Enter Column Name to delete: ")
                    customer_df = customer_df.drop(columns=[column_to_delete])
                    customer_df.to_csv("D\Class12CA\Customer.csv", index=False)
                    print("Column is deleted.")

                elif operation_customer == 5:
                    # View Customer Details
                    # Set display options


                    # Print DataFrame

                    print(customer_df)

                elif operation_customer == 6:
                    # Search Customer
                    search_term = input("Enter Customer Number or Name to search: ")
                    result = customer_df[
                        (customer_df['Cust_no'] == int(search_term)) | (customer_df['Cust_name'].str.contains(search_term, case=False))
                    ]
                    print(result)

                elif operation_customer == 7:
                    # Update Customer Email
                    cust_no_to_update = input("Enter Customer Number to update email: ")
                    new_email = input("Enter the new email: ")
                    customer_df.loc[customer_df['Cust_no'] == int(cust_no_to_update), 'Cust_mail'] = new_email
                    customer_df.to_csv("D\Class12CA\Customer.csv", index=False)
                    print("Email is updated.")

                elif operation_customer == 8:
                    # View Customers by Payment Mode
                    payment_mode_to_view = input("Enter Mode of Payment to view customers: ")
                    result = customer_df[customer_df['Mode_of_payment'] == payment_mode_to_view]
                    print(result)
                    
                elif operation_customer == 9:
                    # Create Line Graph
                    customer_df.plot(x='Cust_no', y='Cust_mobile', kind='line')
                    plt.title('Line Graph of Customer Mobile Numbers')
                    plt.xlabel('Customer Number')
                    plt.ylabel('Customer Mobile Number')
                    plt.show()

                elif operation_customer == 10:
                    # Create Bar Graph
                    customer_df.plot(x='Cust_no', y='Cust_mobile', kind='bar')
                    plt.title('Bar Graph of Customer Mobile Numbers')
                    plt.xlabel('Customer Number')
                    plt.ylabel('Customer Mobile Number')
                    plt.show()

                elif operation_customer == 11:
                    # Create Pie Chart
                    plt.pie(customer_df['Cust_mobile'], labels=customer_df['Cust_no'], autopct='%1.1f%%')
                    plt.title('Pie Chart of Customer Mobile Numbers')
                    plt.show()


                elif operation_customer == 12:
                    # Group By
                    group_by_column_customer = input("Enter column name to group by: ")
                    grouped_data_customer = customer_df.groupby(group_by_column_customer).size().reset_index(name='Count')
                    print(grouped_data_customer)

                elif operation_customer == 13:
                    # Sorting
                    sort_by_column_customer = input("Enter column name to sort by: ")
                    ascending_order_customer = input("Sort in ascending order? (yes/no): ").lower() == 'yes'
                    customer_df = customer_df.sort_values(by=sort_by_column_customer, ascending=ascending_order_customer)
                    print("Data after sorting:")
                    print(customer_df)

                elif operation_customer == 14:
                    # Filtering
                    filter_column_customer = input("Enter column name to filter by: ")
                    filter_value_customer = input("Enter value to filter by: ")
                    filtered_data_customer = customer_df[customer_df[filter_column_customer] == filter_value_customer]
                    print(filtered_data_customer)

                elif operation_customer == 15:
                    # Histogram
                    histogram_column_customer = input("Enter column name for histogram: ")
                    customer_df[histogram_column_customer].hist()
                    plt.title(f'Histogram of {histogram_column_customer}')
                    plt.xlabel(histogram_column_customer)
                    plt.ylabel('Frequency')
                    plt.show()

                elif operation_customer == -1:
                    print("Customer file is closed.")
                    break

                else:
                    print("Invalid operation. Please enter a valid option.")
        elif file_number == 3:
            product_df = pd.read_csv("D\Class12CA\Product.csv")
            pd.set_option('display.max_columns', None)

            while True:
                print("Enter the operation no")
                print("1. Add a row")
                print("2. Delete a row")
                print("3. Add a column")
                print("4. Delete a column")
                print("5. View Product Details")
                print("6. Search Product")
                print("7. Update Product MRP")
                print("8. View Products by Vendor")
                print("9. Create Line Graph")
                print("10. Create Bar Graph")
                print("11. Create Pie Chart")
                print("12. Analyze data by grouping it based on a specific column")
                print("13. Sort the data based on a chosen column in ascending or descending order")
                print("14. Filter the data based on a specific condition and column")
                print("15. Visualize the distribution of a numeric column using a histogram")
                print("-1. Close Product file")

                operation_product = int(input("Enter op no"))

                if operation_product == 1:
                    # Add a row
                    product_code = input("Enter Product Code: ")
                    product_name = input("Enter Product Name: ")
                    product_vendor = input("Enter Product Vendor: ")
                    product_mrp = input("Enter Product MRP: ")

                    new_row = {'ProductCode': product_code, 'ProductName': product_name, 'ProductVendor': product_vendor, 'ProductMrp': product_mrp}
                    product_df = product_df.append(new_row, ignore_index=True)
                    product_df.to_csv("D\Class12CA\Product.csv", index=False)
                    print("Product added successfully.")

                elif operation_product == 2:
                    # Delete a row
                    product_code_to_delete = input("Enter Product Code to delete: ")
                    product_df = product_df[product_df['ProductCode'] != product_code_to_delete]
                    product_df.to_csv("D\Class12CA\Product.csv", index=False)
                    print("Product is deleted.")

                elif operation_product == 3:
                    # Add a column
                    column_name = input("Enter Column Name: ")
                    default_value = input("Enter Default Value for the new column: ")
                    product_df[column_name] = default_value
                    product_df.to_csv("D\Class12CA\Product.csv", index=False)
                    print("Column is added.")

                elif operation_product == 4:
                    # Delete a column
                    column_to_delete = input("Enter Column Name to delete: ")
                    product_df = product_df.drop(columns=[column_to_delete])
                    product_df.to_csv("D\Class12CA\Product.csv", index=False)
                    print("Column is deleted.")

                elif operation_product == 5:
                    # View Product Details
                    print(product_df)

                elif operation_product == 6:
                    # Search Product
                    search_term = input("Enter Product Code or Name to search: ")
                    result = product_df[
                        (product_df['ProductCode'] == search_term) | (product_df['ProductName'].str.contains(search_term, case=False))
                    ]
                    print(result)

                elif operation_product == 7:
                    # Update Product MRP
                    product_code_to_update = input("Enter Product Code to update MRP: ")
                    new_mrp = input("Enter the new MRP: ")
                    product_df.loc[product_df['ProductCode'] == product_code_to_update, 'ProductMrp'] = new_mrp
                    product_df.to_csv("D\Class12CA\Product.csv", index=False)
                    print("MRP is updated.")

                elif operation_product == 8:
                    # View Products by Vendor
                    vendor_to_view = input("Enter Product Vendor to view products: ")
                    result = product_df[product_df['ProductVendor'] == vendor_to_view]
                    print(result)
                elif operation_product == 9:
                    # Create Line Graph
                    plt.plot(product_df['ProductCode'], product_df['ProductMrp'])
                    plt.xlabel('Product Code')
                    plt.ylabel('MRP')
                    plt.title('Product MRP - Line Graph')
                    plt.show()

                elif operation_product == 10:
                    # Create Bar Graph
                    plt.bar(product_df['ProductCode'], product_df['ProductMrp'])
                    plt.xlabel('Product Code')
                    plt.ylabel('MRP')
                    plt.title('Product MRP - Bar Graph')
                    plt.show()

                elif operation_product == 11:
                    # Create Pie Chart
                    plt.pie(product_df['ProductMrp'], labels=product_df['ProductCode'], autopct='%1.1f%%')
                    plt.title('Product MRP - Pie Chart')
                    plt.show()  

                elif operation_product == 12:
                    # Group By
                    group_by_column_product = input("Enter column name to group by: ")
                    grouped_data_product = product_df.groupby(group_by_column_product).size().reset_index(name='Count')
                    print(grouped_data_product)

                elif operation_product == 13:
                    # Sorting
                    sort_by_column_product = input("Enter column name to sort by: ")
                    ascending_order_product = input("Sort in ascending order? (yes/no): ").lower() == 'yes'
                    product_df = product_df.sort_values(by=sort_by_column_product, ascending=ascending_order_product)
                    print("Data after sorting:")
                    print(product_df)

                elif operation_product == 14:
                    # Filtering
                    filter_column_product = input("Enter column name to filter by: ")
                    filter_value_product = input("Enter value to filter by: ")
                    filtered_data_product = product_df[product_df[filter_column_product] == filter_value_product]
                    print(filtered_data_product)

                elif operation_product == 15:
                    # Histogram
                    histogram_column_product = input("Enter column name for histogram: ")
                    product_df[histogram_column_product].hist()
                    plt.title(f'Histogram of {histogram_column_product}')
                    plt.xlabel(histogram_column_product)
                    plt.ylabel('Frequency')
                    plt.show()


                elif operation_product == -1:
                    print("Product file is closed.")
                    break

                else:
                    print("Invalid operation. Please enter a valid option.")
        elif file_number == 4:
            supplier_df = pd.read_csv("D\Class12CA\Supplier.csv")
            pd.set_option('display.max_columns', None)

            while True:
                print("Enter the operation no")
                print("1. Add a row")
                print("2. Delete a row")
                print("3. Add a column")
                print("4. Delete a column")
                print("5. View Supplier Details")
                print("6. Search Supplier")
                print("7. Update Supplier Phone Number")
                print("8. Create Line Graph")
                print("9. Create Bar Graph")
                print("10. Create Pie Chart")
                print("12. Analyze data by grouping it based on a specific column")
                print("13. Sort the data based on a chosen column in ascending or descending order")
                print("14. Filter the data based on a specific condition and column")
                print("15. Visualize the distribution of a numeric column using a histogram")

                print("-1. Close Supplier file")

                operation_supplier = int(input("Enter op no"))

                if operation_supplier == 1:
                    # Add a row
                    supplier_name = input("Enter Supplier Name: ")
                    supplier_address = input("Enter Supplier Address: ")
                    supplier_phone = input("Enter Supplier Phone Number: ")

                    new_row = {'SupplierName': supplier_name, 'SupplierAddress': supplier_address, 'SupplierPhoneNumber': supplier_phone}
                    supplier_df = supplier_df.append(new_row, ignore_index=True)
                    supplier_df.to_csv("D\Class12CA\Supplier.csv", index=False)
                    print("Supplier added successfully.")

                elif operation_supplier == 2:
                    # Delete a row
                    supplier_name_to_delete = input("Enter Supplier Name to delete: ")
                    supplier_df = supplier_df[supplier_df['SupplierName'] != supplier_name_to_delete]
                    supplier_df.to_csv("D\Class12CA\Supplier.csv", index=False)
                    print("Supplier is deleted.")

                elif operation_supplier == 3:
                    # Add a column
                    column_name = input("Enter Column Name: ")
                    default_value = input("Enter Default Value for the new column: ")
                    supplier_df[column_name] = default_value
                    supplier_df.to_csv("D\Class12CA\Supplier.csv", index=False)
                    print("Column is added.")

                elif operation_supplier == 4:
                    # Delete a column
                    column_to_delete = input("Enter Column Name to delete: ")
                    supplier_df = supplier_df.drop(columns=[column_to_delete])
                    supplier_df.to_csv("D\Class12CA\Supplier.csv", index=False)
                    print("Column is deleted.")

                elif operation_supplier == 5:
                    # View Supplier Details
                    print(supplier_df)

                elif operation_supplier == 6:
                    # Search Supplier
                    search_term = input("Enter Supplier Name or Address to search: ")
                    result = supplier_df[
                        (supplier_df['SupplierName'].str.contains(search_term, case=False)) | (supplier_df['SupplierAddress'].str.contains(search_term, case=False))
                    ]
                    print(result)

                elif operation_supplier == 7:
                    # Update Supplier Phone Number
                    supplier_name_to_update = input("Enter Supplier Name to update phone number: ")
                    new_phone_number = input("Enter the new phone number: ")
                    supplier_df.loc[supplier_df['SupplierName'] == supplier_name_to_update, 'SupplierPhoneNumber'] = new_phone_number
                    supplier_df.to_csv("D\Class12CA\Supplier.csv", index=False)
                    print("Phone number is updated.")
                elif operation_supplier == 8:
                    # Create Line Graph
                    plt.plot(supplier_df['SupplierName'], supplier_df['SupplierPhoneNumber'])
                    plt.xlabel('Supplier Name')
                    plt.ylabel('Phone Number')
                    plt.title('Supplier Phone Numbers - Line Graph')
                    plt.show()

                elif operation_supplier == 9:
                    # Create Bar Graph
                    plt.bar(supplier_df['SupplierName'], supplier_df['SupplierPhoneNumber'])
                    plt.xlabel('Supplier Name')
                    plt.ylabel('Phone Number')
                    plt.title('Supplier Phone Numbers - Bar Graph')
                    plt.show()

                elif operation_supplier == 10:
                    # Create Pie Chart
                    plt.pie(supplier_df['SupplierPhoneNumber'], labels=supplier_df['SupplierName'], autopct='%1.1f%%')
                    plt.title('Supplier Phone Numbers - Pie Chart')
                    plt.show()


                elif operation_supplier == 12:
                    # Group By
                    group_by_column_supplier = input("Enter column name to group by: ")
                    grouped_data_supplier = supplier_df.groupby(group_by_column_supplier).size().reset_index(name='Count')
                    print(grouped_data_supplier)

                elif operation_supplier == 13:
                    # Sorting
                    sort_by_column_supplier = input("Enter column name to sort by: ")
                    ascending_order_supplier = input("Sort in ascending order? (yes/no): ").lower() == 'yes'
                    supplier_df = supplier_df.sort_values(by=sort_by_column_supplier, ascending=ascending_order_supplier)
                    print("Data after sorting:")
                    print(supplier_df)

                elif operation_supplier == 14:
                    # Filtering
                    filter_column_supplier = input("Enter column name to filter by: ")
                    filter_value_supplier = input("Enter value to filter by: ")
                    filtered_data_supplier = supplier_df[supplier_df[filter_column_supplier] == filter_value_supplier]
                    print(filtered_data_supplier)

                elif operation_supplier == 15:
                    # Histogram
                    histogram_column_supplier = input("Enter column name for histogram: ")
                    supplier_df[histogram_column_supplier].hist()
                    plt.title(f'Histogram of {histogram_column_supplier}')
                    plt.xlabel(histogram_column_supplier)
                    plt.ylabel('Frequency')
                    plt.show()

                elif operation_supplier == -1:
                    print("Supplier file is closed.")
                    break

                else:
                    print("Invalid operation. Please enter a valid option.")
        elif file_number ==-1:
            print("Thanks for using the app")
            break
    except:
        print("Error")
