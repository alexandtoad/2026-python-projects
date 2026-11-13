passengers = []

def make_passenger():
    name = input("Name please")
    bag_size = int(input("Bag size in KG"))
    security = input("Security true or false!")
    profile = {
        "name": name,
        "bag_size": bag_size,
        "security": security,
    }
    passengers.append(profile)
def staff_menu():
    code_enterd = input("Whats the code")
    if code_enterd == "1527":
        print("Welcome to staff menu!")
        search = input("Who?")
        for person in passengers:
            if person["name"] == search:
                print("Found: ", person)
                choice = input("What would you like to do 1 update name| 2 update bag size 3| update security info |4 exit")
                if choice == "1":
                    person["name"] = input("enter new name")
                elif choice == "2":
                    person["bag_size"] = int(input("Enter new bag size"))
                elif choice == "3":
                    person["security"] = input("enter new security info true / false")
                elif choice == "4":
                    break
                    
    else:
        print("wrong code")
    
while True:
    choice = input("What do you want to do 1. check in passenger| 2 edit passenger| 3 exit")

    if choice == "1":
        make_passenger()
    if choice == "2":
        staff_menu()
    if choice == "3":
        print("Shutting down system....")
        break
    
    
    



