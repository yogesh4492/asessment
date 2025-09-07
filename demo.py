def repairing_order_booking():
    print(welcome.upper().center(55,"-"))
    customer_name=input("Enter Customer Name:- ")
    device_type=input("Enter Device Type:- ")
    issue=input("Enter What is Issue:- ")
    due_date=input("Enter Due Date (dd-mm-yyyy) :-")
    return customer_name,device_type,issue,due_date

welcome="welcome to the repair order booking system"
print(welcome.upper().center(55,"-"))
customer_name=input("Enter Customer Name:- ")
device_type=input("Enter Device Type:- ")
issue=input("Enter What is Issue:- ")
due_date=input("Enter Due Date (dd-mm-yyyy) :-")
print("-"*55)
choice=input("Do You Want To Generate Invoice  Press y :- ").lower()
if choice=='y' or choice=='yes':
    print("invoice".upper().center(55,"-"))
    print(f"Customer Name :- {customer_name.upper()}")
    print(f"Device Type   :- {device_type.upper()} ")
    print(f"Issues        :- {issue.upper()} ")
    print(f"Due Date      :- {due_date}")

else:
    print("thank you".upper().center(55,"-"))

