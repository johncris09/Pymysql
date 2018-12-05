
import pymysql

""" Connection from database """
connection = pymysql.connect(
    host        = 'localhost',      
    user        = 'employee',
    password    = 'employee',
    db          = 'record',
)


""" Inserting Record in Database"""
def add_record(name,gender,address,birthdate,birthplace,status):
##    try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `employee` (`emp_id`, `name`, `gender`, `address`, `birthdate`, `birthplace`, `status`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"
        try:
            cursor.execute(sql, (name,gender,address,birthdate,birthplace,status))
            print("New Record Successfully Added!")
        except:
            print("Oops! Something wrong")

    connection.commit()
##    finally:
##        connection.close()
        

""" Fetch All the Record from the Database """
def view_record():

    """ For Creating Line Purpose """
    hr = ''
    for i in range(147):
        hr = hr + '-'

##    try:
    with connection.cursor() as cursor:
        sql     = "SELECT * FROM `employee`"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print
            print '%80s' % "View of All Contact"
            print hr
            print '%-2s | %-25s | %-6s | %-40s | %-12s | %-30s | %-10s' % ('ID','Name','Gender','Address','Birthdate','Birthplace','Status')
            print hr
            for col in result:
                print '%-2s | %-25s | %-6s | %-40s | %-12s | %-30s | %-10s ' % (col[0], col[1], col[2], col[3], col[4],  col[5], col[6])
            print hr
            print '%80s' % "List of All Contact:" , cursor.rowcount
            
        except:
            print("Oops! Something wrong")

    connection.commit()
##    finally:
##        connection.close()

""" Update selected data  """
def update_record(emp_id):

##    try:
    with connection.cursor() as cursor:
        id_search =  "SELECT *  FROM `employee` WHERE `emp_id` = %s"
        #try:
        cursor.execute(id_search, (emp_id,))
        if cursor.rowcount > 0 :
            col = cursor.fetchall()
            print
            print "Update Record"
            print "Note: Old value will still remain when Pressing Enter"
            print

            """ Variable that holds old value """
            old_name        = col[0][1]
            old_gender      = col[0][2]
            old_address     = col[0][3]
            old_birthdate   = col[0][4]
            old_birthplace  = col[0][5]
            old_status      = col[0][6]

            ## Name
            print "Old Value for Name: ", old_name
            new_name = raw_input("New value for Name: ")
            if len(new_name)>0:
                update_name = new_name
            else:
                update_name = old_name
            ##Gender
            new_gender = "Old Value for Gender: ", old_gender
            if len(new_gender)>0 :
                update_gender = new_gender
            else:
                update_gender = old_gender
            
            ##Address
            new_address = "Old Value for Adress: ", old_address
            if len(new_address) >0:
                update_address = new_address
            else:
                update_address = old_address
            
            ##Birthdate
            new_birthdate = 

        else:
            print "ID '" + emp_id + "' is not Exist!"
        #except:
            #print("Oops! Something wrong")

    connection.commit()
##    finally:
##        connection.close()

""" Delete the selected data """
def delete_record(emp_id):
##    try:
    with connection.cursor() as cursor:
        id_search =  "SELECT *  FROM `employee` WHERE `emp_id` = %s"
        try:
            cursor.execute(id_search, emp_id)
            if cursor.rowcount > 0 :
                del_record = "DELETE FROM `employee` WHERE   emp_id = %s"
                cursor.execute(del_record, emp_id)
                print "New Record Successfully Deleted"
            else:
                print "ID '" + emp_id + "' is not Exist!"
        except:
            print("Oops! Something wrong")

    connection.commit()
##    finally:
##        connection.close()





loop = 1
while loop:

    print"******** MENU ********"
    print"[1] Add Record"
    print"[2] View Record"
    print"[3] Update Record"
    print"[4] Delete Record"
    print"[5] Exit\n"



    choice = raw_input("Enter your choice: ")

    if choice == '1':
        """ Enter All Required Information """
        name            = raw_input('Enter Name: ')
        gender          = raw_input('Enter Gender: ')
        address         = raw_input('Enter Address: ')
        birthdate       = raw_input("Enter Birthdate: [yyyy/mm/dd]: ")
        birthplace      = raw_input("Enter Birth of Place: ")
        status          = raw_input("Enter Status: ")

        """ Call the function add_record to Insert the Entered data to Database """
        add_record(name,gender,address,birthdate,birthplace,status)
    
    elif choice == '2':
        view_record()
    elif choice == '3':
        emp_id = raw_input("What Data you want to Update (Enter ID to proceed) ?: ")
        update_record(emp_id)
    elif choice == '4':
        emp_id = raw_input("What Data you want to Delete (Enter ID to proceed) ?: ")
        delete_record(emp_id)
    
    elif choice == '5':
        print "Program Terminated!!!"
        """ Stop the Program """
        break 
    else:
        print "Invalid Choice"
    


    loop_2 = 1
    while loop_2:
        cont = raw_input("\nDo you wish to continue ? [Y/N]: ").strip()
        if cont in 'Yy':
            loop_2 = 0
            loop = 1
        elif cont in 'Nn':
            print "Program Terminated!!!"
            loop_2 = 0
            loop = 0
        else:
            print 'Invalid Choice'
            loop_2 = 1



