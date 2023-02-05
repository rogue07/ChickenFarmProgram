import os
import time


os.system("clear")

def print_menu():
    print("1. Data Analysis")
    print("2. Environmental Control")
    print("3. Mortality Rate")
    print("4. Egg Production")
    print("5. Health")
    print("6. Financial Tracking")
    print("7. Exit")
    print()

def data_analysis():
    # Code for data analysis
    print("Data Analysis selected")

def environmental_control():
    # Code for environmental control
    print("Environmental Control selected")

def calculate_mortality_rate(total_chickens, dead_chickens):
        return (dead_chickens / total_chickens) * 100
     
     
def mortality_rate():    # Code for mortality rate
    print("Mortality Rate selected")
    total_chickens = int(input("Enter the total number of chickens: "))
    dead_chickens = int(input("Enter the number of dead chickens: "))
    mortality_rate = calculate_mortality_rate(total_chickens, dead_chickens)
    print("The mortality rate is: {:.2f}%".format(mortality_rate))
    time.sleep(5)

    print_menu() 
#    return

def egg_production():
    # Code for egg production
    print("Egg Production selected")

def health():
    # Code for health
    print("Health selected")

def financial_tracking():
    # Code for financial tracking
    print("Financial Tracking selected")

#def chickinput():
#    total_chickens = int(input("Enter the total number of chickens: "))
#    dead_chickens = int(input("Enter the number of dead chickens: "))
#    mortality_rate = dead_chickens / total_chickens * 100
#    return mortality_rate


print_menu()
choice = int(input("Enter your choice [1-7]: "))
if choice == 1:
    data_analysis()
elif choice == 2:
    environmental_control()
elif choice == 3:
    mortality_rate()
elif choice == 4:
    egg_production()
elif choice == 5:
    health()
elif choice == 6:
    financial_tracking()
elif choice == 7:
    print("Invalid choice. Try again.")
#    print()

