print("HELLO USER WELCOME TO PERSONAL EXPENSE TRACKER\n")
print("WHAT DO YOU WANNA DO\n")

x = 1
z = 0.0
a = 0
budget = 0.0  

expenses = {}

def add():
    global z, budget
    if (budget == 0):
        print("\nSet your budget first \n")
        return
    else:
        while True:
            if (z < budget):
                name = str(input("\nEnter expense category or enter exit to leave: "))
                if name.lower() == 'exit':
                    break
                price = float(input("\nEnter the price: "))
                expenses[name] = price
                z += price
            else:
                print("\nYour budget has reached, Change your budget to meet your expenses\n")
                break

def setbudget():
    global budget, x
    if (x == 1):
        budget = float(input("\nEnter your monthly budget: "))
        x += 1
    else:
        y = int(input("\nDo you really wanna change your monthly budget YES: 1 NO: 2 : "))
        if (y == 1):
            budget = float(input("\nEnter new monthly budget: "))

def view():
    if (budget==0) :
        print("\nSet your budget\n")
    else :
        print("\n")
        for name, price in expenses.items():
            print(f"{name}: ₹{price}\n")

def savings():
    global a, budget
    if (budget==0):
        print("\nPlease set your budget first\n")
    elif (z >= budget):
        print("\nNo savings left\n")
    else:
        a = budget - z
        print(f"₹{a} are saved\n")

def delete():
    global z
    while True:
        if (budget==0) :
            print("\nSet your budget\n")
        else:
            for name, price in expenses.items():
                print(f"{name}: ₹{price}\n")
            key_to_remove = str(input("Which category you want to remove: \n"))
            if key_to_remove in expenses:
                b = int(input("Do you really wanna remove this: YES: 1 NO: 2: "))
                if (b == 1):
                    value = expenses.pop(key_to_remove)
                    z -= value
                    print(f"{key_to_remove}: ₹{value} is removed")
                    break
            else:
                print(f"{key_to_remove} not found!")

def main():
    while True:
        print("\n1. Set budget\n")
        print("2. Add expenses\n")
        print("3. Delete expenses\n")
        print("4. View expenses\n")
        print("5. View savings\n")
        print("6. Exit\n")
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            setbudget()
        elif (ch == 2):
            add()
        elif (ch == 3):
            delete()
        elif (ch == 4):
            view()
        elif (ch == 5):
            savings()
        elif (ch == 6):
            break
        else:
            print("Enter valid option\n")
            continue

main()
