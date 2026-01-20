def switcher(day_number):
    switcher_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher_dict.get(day_number, "Invalid day number")

while True:
    print("Menu:")
    print("1. Find day of the week")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter day number        (1-7): "))
        print("Day:", switcher(num))
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")