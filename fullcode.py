import db
import mysql.connector
from flask import Flask, render_template

# Establish database connection
def admin_module():
    print("Admin Module")
    while True:
        print("Admin Services:")
        print("1. Manage Services (View, Search)")
        print("2. Manage Employee (Add, View, Search, Edit, Activate/Deactivate)")
        print("3. Manage Bug (View, Search, Assign Bug to Expert)")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Code for managing services
            def manage_services ( ) :
                print( "Manage Services" )
                while True :
                    print( "1. View Services" )
                    print( "2. Search Services" )
                    print( "3. Add Service" )
                    print( "4. Update Service" )
                    print( "5. Delete Service" )
                    print( "6. Go back" )

                    choice = input( "Enter your choice: " )

                    if choice == "1" :
                     # Code for viewing services
                     def view_services ( ) :
                        print( "View Services" )
                        # Connect to the database
                        cnx = getBTSdatabase()
                        # Create a cursor to execute SQL queries
                        cursor = cnx.cursor()
                        try :
                            # SQL query to fetch all services
                            query = "SELECT * FROM services"
                            # Execute the query
                            cursor.execute( query )
                            # Fetch all the results
                            services = cursor.fetchall()
                            if services :
                                # Display the services
                                for service in services :
                                    print( service )  # Modify this to format the output as per your requirement
                            else :
                                print( "No services found." )

                        except mysql.connector.Error as err :
                            print( "Error occurred while fetching services:" , err )
                        cursor.close( )
                        cnx.close( )
                        pagebreak()
                     view_services( )

                    elif choice == "2" :
                        # Code for searching services
                        def search_services ( ) :
                            print ( "Search Services" )
                            # Connect to the database
                            cnx = getBTSdatabase ( )

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor ( )

                            try :
                                # Prompt the user to enter search criteria
                                criteria = input ( "Enter search criteria: " )

                                # SQL query to search services based on criteria
                                query = f"SELECT * FROM services WHERE name LIKE '%{criteria}%'"

                                # Execute the query
                                cursor.execute ( query )

                                # Fetch all the results
                                search_results = cursor.fetchall ( )

                                if search_results :
                                    # Display the search results
                                    for result in search_results :
                                        print ( result )  # Modify this to format the output as per your requirement
                                else :
                                    print ( "No services found with the specified criteria." )

                            except mysql.connector.Error as err :
                                print ( "Error occurred while searching services:" , err )

                            # Close the cursor and database connection
                            cursor.close ( )
                            cnx.close ( )
                            pagebreak()
                        search_services ( )

                    elif choice == "3" :
                        # Code for adding a new service
                        def add_service ( ) :
                            print( "Add Service" )
                            # Connect to the database
                            cnx = getBTSdatabase()

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor( )

                            try :
                                # Prompt the user to enter service details
                                service_name = input( "Enter service name: " )
                                service_description = input( "Enter service description: " )

                                # SQL query to add a new service
                                query = f"INSERT INTO services (name, description) VALUES ('{service_name}', '{service_description}')"

                                # Execute the query
                                cursor.execute( query )

                                # Commit the changes to the database
                                cnx.commit( )

                                print( "Service added successfully." )

                            except mysql.connector.Error as err :
                                print( "Error occurred while adding a service:" , err )

                            # Close the cursor and database connection
                            cursor.close( )
                            cnx.close( )
                            pagebreak()
                        add_service( )
                    elif choice == "4" :
                        # Code for updating a service

                        def update_service ( ) :
                            print( "Update Service" )
                            # Connect to the database
                            cnx = getBTSdatabase()

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor( )

                            try :
                                # Prompt the user to enter the service ID to update
                                service_id = input( "Enter the service ID to update: " )

                                # Prompt the user to enter the updated service details
                                updated_name = input( "Enter updated service name: " )
                                updated_description = input( "Enter updated service description: " )

                                # SQL query to update the service
                                query = f"UPDATE services SET name = '{updated_name}', description = '{updated_description}' WHERE id = '{service_id}'"

                                # Execute the query
                                cursor.execute( query )

                                # Commit the changes to the database
                                cnx.commit( )

                                print( "Service updated successfully." )

                            except mysql.connector.Error as err :
                                print( "Error occurred while updating a service:" , err )

                            # Close the cursor and database connection
                            cursor.close( )
                            cnx.close( )
                            pagebreak()
                        update_service( )
                    elif choice == "5" :
                        # Code for deleting a service
                        def delete_service ( ) :
                            print( "Delete Service" )
                            # Connect to the database
                            cnx = getBTSdatabase()

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor( )

                            try :
                                # Prompt the user to enter the service ID to delete
                                service_id = input( "Enter the service ID to delete: " )

                                # SQL query to delete the service
                                query = f"DELETE FROM services WHERE id = '{service_id}'"

                                # Execute the query
                                cursor.execute( query )

                                # Commit the changes to the database
                                cnx.commit( )

                                print( "Service deleted successfully." )

                            except mysql.connector.Error as err :
                                print( "Error occurred while deleting a service:" , err )

                            # Close the cursor and database connection
                            cursor.close( )
                            cnx.close( )
                            pagebreak()
                        delete_service( )

                    elif choice == "6" :
                        # Go back to the previous menu
                        break
                    else :
                        print( "Invalid choice. Please try again." )

            pagebreak()
            manage_services()

        elif choice == "2":
            # Code for managing employees
            def manage_employees ( ) :
                print ( "Manage Employees" )
                print ( "1. Add New (Admin or Expert)" )
                print ( "2. View All" )
                print ( "3. Search - by Employee Name" )
                print ( "4. Search - by Employee Login Id" )
                print ( "5. Search - by Employee Type" )
                print ( "6. Activate or Deactivate" )
                print ( "7. Change Password" )

                employee_choice = input ( "Enter your choice: " )

                if employee_choice == "1" :
                    # Code for adding a new employee
                    def add_employee ( ) :
                            # Code for adding a new employee
                            # Connect to the database
                            cnx = getBTSdatabase()
                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor ( )
                            # Get employee details from user input
                            empLoginId = input ( "Enter employee login ID: " )
                            empPassword = input ( "Enter employee password: " )
                            empType = input ( "Enter employee type (Admin or Expert): " )
                            empName = input ( "Enter employee name: " )
                            empPhone = input ( "Enter employee phone number: " )
                            empEmail = input ( "Enter employee email address: " )

                            # Insert the employee details into the database
                            insert_query = "INSERT INTO employee (empLoginId, empPassword, empType, empName, empPhone, empEmail) VALUES (%s, %s, %s, %s, %s, %s)"
                            values = (empLoginId , empPassword , empType , empName , empPhone , empEmail)      ##empLoginId, empPassword, empType, empName, empPhone, empEmail
                            cursor.execute ( insert_query , values )
                            cnx.commit()

                            print ( "Employee added successfully." )

                            # Close the cursor and database connection
                            cursor.close ( )
                            cnx.close ( )
                            pagebreak()
                    add_employee ( )

                elif employee_choice == "2" :
                    # Code for viewing all employees
                    def view_all_employees ( ) :
                        # Code for viewing all employees
                            # Connect to the database
                            cnx = getBTSdatabase ( )

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor ( )

                            # Retrieve all employees from the database
                            select_query = "SELECT * FROM employee"
                            cursor.execute ( select_query )
                            results = cursor.fetchall ( )

                            # Display the retrieved employee data
                            if results :
                                print ( "All Employees:" )
                                for row in results :
                                    print ( "Employee Login ID:" , row [ 0] )
                                    print ( "Employee Password:" , row [ 1 ] )
                                    print ( "Employee Type:" , row [ 2 ] )
                                    print ( "Employee Name:" , row [ 3 ] )
                                    print ( "Employee Phone:" , row [ 4 ] )
                                    print ( "Employee Email:" , row [ 5 ] )
                                    print ( "Employee Status:" , row [ 6 ] )
                                    print ( "----------------------" )
                            else :
                                print ( "No employees found." )

                            # Close the cursor and database connection
                            cursor.close ( )
                            cnx.close ( )
                            pagebreak()
                    view_all_employees ( )

                elif employee_choice == "3" :
                    # Code for searching employees by name
                    def search_employee_by_name ( ) :
                        # Code for searching employees by name
                        emp_name = input ( "Enter employee name: " )

                        # Connect to the database
                        cnx = getBTSdatabase ( )

                        # Create a cursor to execute SQL queries
                        cursor = cnx.cursor ( )

                        # Retrieve employees by name from the database
                        select_query = "SELECT * FROM employee WHERE empName LIKE %s"
                        cursor.execute ( select_query , (f'%{emp_name}%' ,) )
                        results = cursor.fetchall ( )

                        # Display the retrieved employee data
                        if results :
                            print ( "Employees with name containing" , emp_name + ":" )
                            for row in results :
                                print ( "Employee ID:" , row [ 0 ] )
                                print ( "Employee Login ID:" , row [ 1 ] )
                                print ( "Employee Password:" , row [ 2 ] )
                                print ( "Employee Type:" , row [ 3 ] )
                                print ( "Employee Phone:" , row [ 4 ] )
                                print ( "Employee Email:" , row [ 5 ] )
                                print ( "Employee Status:" , row [ 6 ] )
                                print ( "----------------------" )
                        else :
                            print ( "No employees found with name containing" , emp_name )

                        # Close the cursor and database connection
                        cursor.close ( )
                        cnx.close ( )
                        pagebreak ( )
                    search_employee_by_name ( )

                elif employee_choice == "4" :
                    # Code for searching employees by login ID
                    def search_employee_by_login_id ( ) :
                        # Code for searching employees by login ID
                        emp_login_id = input ( "Enter employee login ID: " )

                        # Connect to the database
                        cnx = getBTSdatabase ( )

                        # Create a cursor to execute SQL queries
                        cursor = cnx.cursor ( )

                        # Retrieve employee by login ID from the database
                        select_query = "SELECT * FROM employee WHERE empLoginId = %s"
                        cursor.execute ( select_query , (emp_login_id ,) )
                        result = cursor.fetchone ( )

                        # Display the retrieved employee data
                        if result :
                            print ( "Employee ID:" , result [ 0 ] )
                            print ( "Employee Password:" , result [ 1 ] )
                            print ( "Employee Type:" , result [ 2 ] )
                            print ( "Employee Name:" , result [ 3 ] )
                            print ( "Employee Phone:" , result [ 4 ] )
                            print ( "Employee Email:" , result [ 5 ] )
                            print ( "Employee Status:" , result [ 6 ] )
                        else :
                            print ( "No employee found with login ID" , emp_login_id )

                        # Close the cursor and database connection
                        cursor.close ( )
                        cnx.close ( )
                        pagebreak()
                    pass
                    search_employee_by_login_id ( )

                elif employee_choice == "5" :
                    # Code for searching employees by type
                    def search_employee_by_type ( ) :
                        # Code for searching employees by type
                        emp_type = input ( "Enter employee type (ADMIN/EXPERT): " )

                        # Connect to the database
                        cnx = getBTSdatabase ( )

                        # Create a cursor to execute SQL queries
                        cursor = cnx.cursor ( )

                        # Retrieve employees by type from the database
                        select_query = "SELECT * FROM employee WHERE empType = %s"
                        cursor.execute ( select_query , (emp_type ,) )
                        results = cursor.fetchall ( )

                        # Display the retrieved employee data
                        if results :
                            print ( "Employees of type" , emp_type + ":" )
                            for row in results :
                                print ( "Employee ID:" , row [ 0 ] )
                                print ( "Employee Name:" , row [ 3 ] )
                                print ( "Employee Phone:" , row [ 4 ] )
                                print ( "Employee Email:" , row [ 5 ] )
                                print ( "Employee Status:" , row [ 6 ] )
                                print ( "----------------------" )
                        else :
                            print ( "No employees found for type" , emp_type )

                        # Close the cursor and database connection
                        cursor.close ( )
                        cnx.close ( )
                        pagebreak()
                    pass
                    search_employee_by_type ( )

                elif employee_choice == "6" :
                    # Code for activating or deactivating an employee
                    def activate_deactivate_employee ( ) :
                        # Code for activating or deactivating an employee
                        emp_login_id = input ( "Enter employee login ID: " )
                        action = input ( "Enter 'activate' or 'deactivate': " )

                        # Connect to the database
                        cnx = getBTSdatabase ( )

                        # Create a cursor to execute SQL queries
                        cursor = cnx.cursor ( )

                        # Update the employee status in the database
                        update_query = "UPDATE employee SET empStatus = %s WHERE empLoginId = %s"
                        cursor.execute ( update_query , (action.upper ( ) , emp_login_id) )
                        cnx.commit ( )

                        # Close the cursor and database connection
                        cursor.close ( )
                        cnx.close ( )

                        print ( "Employee status updated successfully." )

                    pass
                    pagebreak ( )
                    activate_deactivate_employee ( )

                elif employee_choice == "7" :
                    # Code for changing employee password
                    def change_employee_password ():
                        # Code for changing employee password
                        emp_login_id = input ( "Enter employee login ID: " )
                        new_password = input ( "Enter new password: " )

                        # Connect to the database
                        cnx = getBTSdatabase ( )

                        # Create a cursor to execute SQL queries
                        cursor = cnx.cursor ( )

                        # Update the employee password in the database
                        update_query = "UPDATE employee SET empPassword = %s WHERE empLoginId = %s"
                        cursor.execute ( update_query , (new_password , emp_login_id) )
                        cnx.commit ( )

                        # Close the cursor and database connection
                        cursor.close ( )
                        cnx.close ( )

                        print ( "Employee password updated successfully." )

                    pass
                    pagebreak ( )
                    change_employee_password ( )
            manage_employees()

        elif choice == "3":
            # Code for managing bugs
            def manage_bugs ( ) :
                print ( "Manage Bugs" )

                # Code for managing bugs goes here
                while True :
                    print ( "1. View All Bugs" )
                    print ( "2. Search Bugs by Bug ID" )
                    print ( "3. Search Bugs by Status" )
                    print ( "4. Assign Bug to Expert" )
                    print ( "5. Go back" )

                    choice = input ( "Enter your choice: " )

                    if choice == "1" :
                        # Code for viewing all bugs
                        def view_all_bugs ( ) :
                            print ( "View All Bugs" )
                            # Fetch and display all bugs from the database
                            # Example code:
                            # Connect to the database
                            cnx = getBTSdatabase()

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor ( )

                            try :
                                # SQL query to fetch all bugs
                                query = "SELECT * FROM Bug"

                                # Execute the query
                                cursor.execute ( query )

                                # Fetch all the bugs
                                Bug = cursor.fetchall ( )

                                if Bug :
                                    # Display the bug details
                                    for Bug in Bug :
                                        print ( Bug )  # Modify this to format the output as per your requirement
                                else :
                                    print ( "No bugs found." )

                            except mysql.connector.Error as err :
                                print ( "Error occurred while viewing all bugs:" , err )

                            # Close the cursor and database connection
                            cursor.close ( )
                            cnx.close ( )
                            pagebreak ( )

                        view_all_bugs ( )
                    elif choice == "2" :
                        # Code for searching bugs by bug ID

                        def search_bugs_by_id ( ) :
                            print ( "Search Bugs by Bug ID" )
                            # Prompt the user to enter the bug ID to search
                            bugId = input ( "Enter the bug ID: " )

                            # Search bugs by bug ID in the database
                            # Example code:
                            # Connect to the database
                            cnx = getBTSdatabase()

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor ( )

                            try :
                                # SQL query to search bugs by bug ID
                                query = f"SELECT * FROM Bug WHERE bugId = '{bugId}'"

                                # Execute the query
                                cursor.execute ( query )

                                # Fetch the bug
                                Bug = cursor.fetchone ( )

                                if Bug :
                                    print ( Bug )  # Modify this to format the output as per your requirement
                                else :
                                    print ( "Bug not found." )

                            except mysql.connector.Error as err :
                                print ( "Error occurred while searching bugs by ID:" , err )

                            # Close the cursor and database connection
                            cursor.close ( )
                            cnx.close ()
                        search_bugs_by_id ( )
                    elif choice == "3" :
                        # Code for searching bugs by status
                        def search_bugs_by_status ( ):
                         print ( "Search Bugs by Status" )
                        # Prompt the user to enter the bug status to search
                         bugStatus = input ( "Enter the bug status: " )

                        # Search bugs by status in the database
                        # Connect to the database
                         cnx = getBTSdatabase()

                        # Create a cursor to execute SQL queries
                         cursor = cnx.cursor ( )

                         try :
                            # SQL query to search bugs by status
                            query = f"SELECT * FROM Bug WHERE bugStatus = '{bugStatus}'"

                            # Execute the query
                            cursor.execute ( query )

                            # Fetch all the bugs
                            Bug = cursor.fetchall ( )

                            if Bug :
                                # Display the bug details
                                for Bug in Bug :
                                    print ( Bug )  # Modify this to format the output as per your requirement
                            else :
                                print ( "No bugs found with the specified status." )

                         except mysql.connector.Error as err :
                            print ( "Error occurred while searching bugs by status:" , err )

                        # Close the cursor and database connection
                         cursor.close ( )
                         cnx.close ( )
                         pagebreak ( )
                        search_bugs_by_status ( )

                    elif choice == "4" :
                        # Code for assigning bug to expert
                        from datetime import datetime

                        def assign_bug_to_expert ( ) :
                            print ( "Assign Bug to Expert" )
                            # Prompt the user to enter the bug ID and expert ID
                            bugId = input ( "Enter the bug ID: " )
                            expertLoginId = input ( "Enter the expert ID: " )

                            # Assign bug to an expert in the database
                            # Connect to the database
                            cnx = getBTSdatabase()

                            # Create a cursor to execute SQL queries
                            cursor = cnx.cursor ( )

                            try :
                                # SQL query to update the bug with the expert ID
                                expertAssignedDate = datetime.now ( )
                                query = f"UPDATE Bug SET expertLoginId = '{expertLoginId}', expertAssignedDate = '{expertAssignedDate}' WHERE bugId = '{bugId}'"

                                # Execute the query
                                cursor.execute ( query )

                                # Commit the changes to the database
                                cnx.commit ( )

                                print ( "Bug assigned to expert successfully." )

                            except mysql.connector.Error as err :
                                print ( "Error occurred while assigning bug to expert:" , err )

                                # Close the cursor and database connection
                            cursor.close ( )
                            cnx.close ( )
                            pagebreak ( )

                        assign_bug_to_expert ( )

                    elif choice == "5" :
                        # Go back to the previous menu
                        break
                    else :
                        print ( "Invalid choice. Please try again." )
            manage_bugs()

        elif choice == "4":
            # Code for logout
            from flask import session , redirect , url_for

            def logout ( ) :
                print ( "Logout" )
                # Clear session data
                session.clear ( )
                # Redirect to the login page
                return redirect ( url_for ( 'login' ) )

            logout ( )

            break
        else:
            print("Invalid choice. Please try again.")


# Customer Module
def customer_module():
    print("Customer Module")
    while True:
        print("Customer Services:")
        print("1. Create Account")
        print("2. Update Account")
        print("3. Post New Bug")
        print("4. View All Bugs")
        print("5. Search Bugs based on status")
        print("6. View Bug Solution")
        print("7. Change Password")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":


            def create_account ( ) :
                print( "Create Account" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # Prompt the admin to enter the customer details
                    cust_login_id = input( "Enter customer login ID: " )
                    cust_password = input( "Enter customer password: " )
                    cust_name = input( "Enter customer name: " )
                    cust_age = int( input( "Enter customer age: " ) )
                    cust_phone = input( "Enter customer phone number: " )
                    cust_email = input( "Enter customer email: " )

                    # SQL query to insert the customer details into the database
                    query = f"INSERT INTO customer (custLoginId, custPassword, custName, custAge, custPhone, custEmail) " \
                            f"VALUES ('{cust_login_id}', '{cust_password}', '{cust_name}', {cust_age}, '{cust_phone}', '{cust_email}')"

                    # Execute the query
                    cursor.execute( query )

                    # Commit the changes to the database
                    cnx.commit( )

                    print( "Account created successfully." )

                except mysql.connector.Error as err :
                    print( "Error occurred while creating an account:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )
            create_account ()



        elif choice == "2":


            def update_account ( ) :
                print( "Update Account" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # Prompt the admin to enter the customer login ID
                    cust_login_id = input( "Enter customer login ID: " )

                    # SQL query to check if the customer exists
                    check_query = f"SELECT * FROM customer WHERE custLoginId = '{cust_login_id}'"

                    # Execute the query
                    cursor.execute( check_query )

                    # Fetch the result
                    result = cursor.fetchone( )

                    if result :
                        print( "Customer found." )
                        print( "Enter new account details:" )

                        # Prompt the admin to enter the updated customer details
                        cust_password = input( "Enter customer password: " )
                        cust_name = input( "Enter customer name: " )
                        cust_age = int( input( "Enter customer age: " ) )
                        cust_phone = input( "Enter customer phone number: " )
                        cust_email = input( "Enter customer email: " )

                        # SQL query to update the customer details in the database
                        update_query = f"UPDATE customer SET custPassword = '{cust_password}', " \
                                       f"custName = '{cust_name}', custAge = {cust_age}, " \
                                       f"custPhone = '{cust_phone}', custEmail = '{cust_email}' " \
                                       f"WHERE custLoginId = '{cust_login_id}'"

                        # Execute the query
                        cursor.execute( update_query )

                        # Commit the changes to the database
                        cnx.commit( )

                        print( "Account details updated successfully." )
                    else :
                        print( "Customer not found." )

                except mysql.connector.Error as err :
                    print( "Error occurred while updating account details:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )

            update_account ( )



        elif choice == "3":

            def post_new_bug ( ) :
                print( "Post New Bug" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # Prompt the customer to enter the bug details
                    cust_login_id = input( "Enter your login ID: " )
                    product_name = input( "Enter product name: " )
                    bug_desc = input( "Enter bug description: " )

                    # SQL query to insert the bug details into the database
                    query = f"INSERT INTO bug (custLoginId, productName, bugDesc) " \
                            f"VALUES ('{cust_login_id}', '{product_name}', '{bug_desc}')"

                    # Execute the query
                    cursor.execute( query )

                    # Commit the changes to the database
                    cnx.commit( )

                    print( "Bug posted successfully." )

                except mysql.connector.Error as err :
                    print( "Error occurred while posting a new bug:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )
            post_new_bug ( )


        elif choice == "4":

            def view_all_bugs ( ) :
                print( "View All Bugs" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # SQL query to fetch all bugs from the database
                    query = "SELECT * FROM bug"

                    # Execute the query
                    cursor.execute( query )

                    # Fetch all the bugs
                    bugs = cursor.fetchall( )

                    if bugs :
                        # Print the bug details
                        for bug in bugs :
                            bug_id = bug [ 0 ]
                            bug_posting_date = bug [ 1 ]
                            cust_login_id = bug [ 2 ]
                            bug_status = bug [ 3 ]
                            product_name = bug [ 4 ]
                            bug_desc = bug [ 5 ]
                            expert_assigned_date = bug [ 6 ]
                            expert_login_id = bug [ 7 ]
                            bug_solved_date = bug [ 8 ]
                            solution = bug [ 9 ]

                            print( f"Bug ID: {bug_id}" )
                            print( f"Posting Date: {bug_posting_date}" )
                            print( f"Customer Login ID: {cust_login_id}" )
                            print( f"Bug Status: {bug_status}" )
                            print( f"Product Name: {product_name}" )
                            print( f"Bug Description: {bug_desc}" )
                            print( f"Expert Assigned Date: {expert_assigned_date}" )
                            print( f"Expert Login ID: {expert_login_id}" )
                            print( f"Bug Solved Date: {bug_solved_date}" )
                            print( f"Solution: {solution}" )
                            print( )

                    else :
                        print( "No bugs found." )

                except mysql.connector.Error as err :
                    print( "Error occurred while viewing all bugs:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )
            view_all_bugs()



        elif choice == "5":


            def search_bugs_by_status ( ) :
                print( "Search Bugs by Status" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # Prompt the admin to enter the bug status
                    bug_status = input( "Enter bug status to search: " )

                    # SQL query to search bugs by status
                    query = f"SELECT * FROM bug WHERE bugStatus = '{bug_status}'"

                    # Execute the query
                    cursor.execute( query )

                    # Fetch the bugs
                    bugs = cursor.fetchall( )

                    if bugs :
                        # Print the bug details
                        for bug in bugs :
                            bug_id = bug [ 0 ]
                            bug_posting_date = bug [ 1 ]
                            cust_login_id = bug [ 2 ]
                            bug_status = bug [ 3 ]
                            product_name = bug [ 4 ]
                            bug_desc = bug [ 5 ]
                            expert_assigned_date = bug [ 6 ]
                            expert_login_id = bug [ 7 ]
                            bug_solved_date = bug [ 8 ]
                            solution = bug [ 9 ]

                            print( f"Bug ID: {bug_id}" )
                            print( f"Posting Date: {bug_posting_date}" )
                            print( f"Customer Login ID: {cust_login_id}" )
                            print( f"Bug Status: {bug_status}" )
                            print( f"Product Name: {product_name}" )
                            print( f"Bug Description: {bug_desc}" )
                            print( f"Expert Assigned Date: {expert_assigned_date}" )
                            print( f"Expert Login ID: {expert_login_id}" )
                            print( f"Bug Solved Date: {bug_solved_date}" )
                            print( f"Solution: {solution}" )
                            print( )

                    else :
                        print( "No bugs found with the specified status." )

                except mysql.connector.Error as err :
                    print( "Error occurred while searching bugs by status:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )
            search_bugs_by_status ( )



        elif choice == "6":


            def view_bug_solution ( ) :
                print( "View Bug Solution" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # Prompt the customer to enter the bug ID
                    bug_id = input( "Enter the Bug ID to view the solution: " )

                    # SQL query to fetch the bug solution from the database
                    query = f"SELECT solution FROM bug WHERE bugId = {bug_id}"

                    # Execute the query
                    cursor.execute( query )

                    # Fetch the bug solution
                    bug_solution = cursor.fetchone( )

                    if bug_solution :
                        solution = bug_solution [ 0 ]
                        print( f"Bug Solution: {solution}" )
                    else :
                        print( "No solution found for the specified bug ID." )

                except mysql.connector.Error as err :
                    print( "Error occurred while viewing bug solution:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )
            view_bug_solution ( )



        elif choice == "7":


            def change_password ( ) :
                print( "Change Password" )

                # Connect to the database
                cnx = getBTSdatabase()

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor( )

                try :
                    # Prompt the customer to enter the current password
                    current_password = input( "Enter current password: " )

                    # Prompt the customer to enter the new password
                    new_password = input( "Enter new password: " )

                    # Prompt the customer to confirm the new password
                    confirm_password = input( "Confirm new password: " )

                    # Check if the new password and confirm password match
                    if new_password == confirm_password :
                        # SQL query to update the password in the customer table
                        query = f"UPDATE customer SET custPassword = '{new_password}' WHERE custLoginId = 'CU2001'"

                        # Execute the query
                        cursor.execute( query )
                        cnx.commit( )

                        print( "Password changed successfully." )
                    else :
                        print( "New password and confirm password do not match. Please try again." )

                except mysql.connector.Error as err :
                    print( "Error occurred while changing password:" , err )

                # Close the cursor and database connection
                cursor.close( )
                cnx.close( )
                pagebreak ( )
            change_password ( )

        elif choice == "8":
            break

# Expert Module
def expert_module():
    print("Expert Module")
    while True:
        print("Expert Services:")
        print("1. View Assigned Bugs")
        print("2. Filter Assigned Bugs based on status")
        print("3. Solve the Bug")
        print("4. Change Password")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Code for viewing assigned bugs
            def view_assigned_bugs ( ) :
                print ( "View Assigned Bugs" )

                # Connect to the database
                cnx = getBTSdatabase ( )
                # Create a cursor to execute SQL queries
                cursor = cnx.cursor ( )

                try :
                    # SQL query to fetch assigned bugs for the expert
                    query = "SELECT bugId, productName, bugDesc FROM bug WHERE expertLoginId = 'EX3001'"

                    # Execute the query
                    cursor.execute ( query )

                    # Fetch all the results
                    assigned_bugs = cursor.fetchall ( )

                    if assigned_bugs :
                        # Display the bug details
                        for bug in assigned_bugs :
                            bug_id , product_name , bug_desc = bug
                            print ( f"Bug ID: {bug_id}" )
                            print ( f"Product Name: {product_name}" )
                            print ( f"Bug Description: {bug_desc}" )
                            print ( "------------------------------" )
                    else :
                        print ( "No assigned bugs found." )

                except mysql.connector.Error as err :
                    print ( "Error occurred while fetching assigned bugs:" , err )

                # Close the cursor and database connection
                cursor.close ( )
                cnx.close ( )
                pagebreak ( )
            view_assigned_bugs()

        elif choice == "2":
            # Code for filtering assigned bugs based on status
            def filter_assigned_bugs ( ) :
                print ( "Filter Assigned Bugs based on status" )

                # Connect to the database
                cnx = getBTSdatabase ( )
                # Create a cursor to execute SQL queries
                cursor = cnx.cursor ( )

                try :
                    # Prompt the user to enter the bug status to filter
                    status = input ( "Enter the bug status to filter: " )

                    # SQL query to fetch assigned bugs for the expert based on status
                    query = f"SELECT bugId, productName, bugDesc FROM bug WHERE expertLoginId = 'EX3001' AND bugStatus = '{status}'"

                    # Execute the query
                    cursor.execute ( query )

                    # Fetch all the results
                    filtered_bugs = cursor.fetchall ( )

                    if filtered_bugs :
                        # Display the filtered bug details
                        for bug in filtered_bugs :
                            bug_id , product_name , bug_desc = bug
                            print ( f"Bug ID: {bug_id}" )
                            print ( f"Product Name: {product_name}" )
                            print ( f"Bug Description: {bug_desc}" )
                            print ( "------------------------------" )
                    else :
                        print ( "No bugs found with the specified status." )

                except mysql.connector.Error as err :
                    print ( "Error occurred while filtering assigned bugs:" , err )

                # Close the cursor and database connection
                cursor.close ( )
                cnx.close()
                pagebreak()
            filter_assigned_bugs()

        elif choice == "3":
            # Code for solving a bug
            def solve_bug ( ) :
                print ( "Solve the Bug" )

                # Connect to the database
                cnx = getBTSdatabase ( )

                # Create a cursor to execute SQL queries
                cursor = cnx.cursor ( )

                try :
                    # Prompt the user to enter the bug ID to solve
                    bug_id = input ( "Enter the bug ID to solve: " )

                    # Prompt the user to enter the bug solution
                    solution = input ( "Enter the bug solution: " )

                    # SQL query to update the bug status and solution
                    query = f"UPDATE bug SET bugStatus = 'Solved', solution = '{solution}', bugSolvedDate = NOW() WHERE bugId = '{bug_id}'"

                    # Execute the query
                    cursor.execute ( query )

                    # Commit the changes to the database
                    cnx.commit ( )

                    print ( "Bug solved successfully." )

                except mysql.connector.Error as err :
                    print ( "Error occurred while solving the bug:" , err )

                # Close the cursor and database connection
                cursor.close ( )
                cnx.close ( )
                pagebreak()
                pass
            solve_bug()

        elif choice == "4":
            # Code for changing password
            def change_password ( ) :
                print ( "Change Password" )

                # Connect to the database
                cnx = getBTSdatabase ( )
                # Create a cursor to execute SQL queries
                cursor = cnx.cursor ( )

                try :
                    # Prompt the user to enter the employee login ID
                    emp_login_id = input ( "Enter your login ID: " )

                    # Prompt the user to enter the new password
                    new_password = input ( "Enter your new password: " )

                    # SQL query to update the employee's password
                    query = f"UPDATE employee SET empPassword = '{new_password}' WHERE empLoginId = '{emp_login_id}'"

                    # Execute the query
                    cursor.execute ( query )

                    # Commit the changes to the database
                    cnx.commit ()

                    print ( "Password changed successfully." )

                except mysql.connector.Error as err :
                    print ( "Error occurred while changing password:" , err )

                # Close the cursor and database connection
                cursor.close ( )
                cnx.close ( )
                pagebreak()
            change_password()

        elif choice == "5":
            # Code for logout


            def logout ( ) :
                print ( "Logout" )
                # Clear session data


            logout ()
            break




# Additional code for other functionalities in the expert module
def getBTSdatabase():
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="bug_system_db ")
  return db
def pagebreak():
    print("---------------------------------------------------")
    print("\n")
# Login Module

def login_module():

    print("LOGIN MODULE")
    print ( "\n"
            )
    print("1. Login")
    print("2. Sign-Up")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Existing login logic
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        cnx = getBTSdatabase()
        cursor = cnx.cursor()

        # Check against the admin table
        query = "SELECT empType FROM employee WHERE empLoginId = %s AND empPassword = %s AND empLoginId LIKE 'AD%'"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            user_type = "ADMIN"
        else:
            # Check against the expert table
            query = "SELECT empType FROM employee WHERE empLoginId = %s AND empPassword = %s AND empLoginId LIKE 'EX%'"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                user_type = "EXPERT"
            else:
                # Check against the customer table
                query = "SELECT custName FROM customer WHERE custLoginId = %s AND custPassword = %s AND custLoginId LIKE 'CU%'"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()

                if result:
                    user_type = "CUSTOMER"
                else:
                    print("Invalid username or password")
                    return

        # Based on the user type, redirect to the respective module
        if user_type == "ADMIN":
            admin_module()
        elif user_type == "EXPERT":
            expert_module()
        elif user_type == "CUSTOMER":
            customer_module()

    elif choice == "2":
        # Sign-Up logic
        def signup_module ( ) :
            print ( "Sign-Up Module" )
            user_type = input ( "Enter user type (ADMIN/EXPERT/CUSTOMER): " )
            username = input ( "Enter username: " )
            password = input ( "Enter password: " )

            cnx = getBTSdatabase ( )
            cursor = cnx.cursor ( )

            if user_type == "ADMIN" :
                # Check if the username starts with 'AD'
                if username.startswith ( "AD" ) :
                    try :
                        # Insert the admin details into the employee table
                        query = "INSERT INTO employee (empLoginId, empPassword, empType) VALUES (%s, %s, %s)"
                        cursor.execute ( query , (username , password , user_type) )
                        cnx.commit ( )
                        print ( "Admin user created successfully." )
                    except mysql.connector.Error as err :
                        print ( "Error occurred while creating admin user:" , err )
                else :
                    print ( "Invalid username format for an admin user." )
            elif user_type == "EXPERT" :
                # Check if the username starts with 'EX'
                if username.startswith ( "EX" ) :
                    try :
                        # Insert the expert details into the employee table
                        query = "INSERT INTO employee (empLoginId, empPassword, empType) VALUES (%s, %s, %s)"
                        cursor.execute ( query , (username , password , user_type) )
                        cnx.commit ( )
                        print ( "Expert user created successfully." )
                    except mysql.connector.Error as err :
                        print ( "Error occurred while creating expert user:" , err )
                else :
                    print ( "Invalid username format for an expert user." )
            elif user_type == "CUSTOMER" :
                # Check if the username starts with 'CU'
                if username.startswith ( "CU" ) :
                    try :
                        # Insert the customer details into the customer table
                        query = "INSERT INTO customer (custLoginId, custPassword) VALUES (%s, %s)"
                        cursor.execute ( query , (username , password) )
                        cnx.commit ( )
                        print ( "Customer user created successfully." )
                    except mysql.connector.Error as err :
                        print ( "Error occurred while creating customer user:" , err )
                else :
                    print ( "Invalid username format for a customer user." )
            else :
                print ( "Invalid user type." )

            cursor.close ( )
            cnx.close ( )

        signup_module()
        print("\n")
        login_module ()

    else:
        print("Invalid choice. Please try again.")
login_module()


