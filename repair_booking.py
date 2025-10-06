def repairing_order_booking():
    print(welcome.upper().center(55,"-"))
    customer_name=input("Enter Customer Name:- ")
    device_type=input("Enter Device Type:- ")
    issue=input("Enter What is Issue:- ")
    due_date=input("Enter Due Date (dd-mm-yyyy) :-")
    return {'customer_name':customer_name,'device_type':device_type,'issue':issue,'due_date':due_date}

welcome="welcome to the repair order booking system"
# print(welcome.upper().center(55,"-"))
dicts=repairing_order_booking()
# customer_name=input("Enter Customer Name:- ")
# device_type=input("Enter Device Type:- ")
# issue=input("Enter What is Issue:- ")
# due_date=input("Enter Due Date (dd-mm-yyyy) :-")
print("-"*55)
choice=input("Do You Want To Generate Invoice  Press y :- ").lower()
if choice=='y' or choice=='yes':
    print("invoice".upper().center(55,"-"))
    print(f"Customer Name :- {dicts['customer_name'].upper()}")
    print(f"Device Type   :- {dicts['device_type'].upper()} ")
    print(f"Issues        :- {dicts['issue'].upper()} ")
    print(f"Due Date      :- {dicts['due_date']}")
    print("thank you".upper().center(55,"-"))

else:
    print("thank you".upper().center(55,"-"))

