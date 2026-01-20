def calculate_bill(units):
    if units <= 100:
        charge = units * 1
    elif units <= 300:
        charge = (100 * 1) + ((units - 100) * 2)
    else:
        charge = (100 * 1) + (200 * 2) + ((units - 300) * 3)
    return charge

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
units = int(input("Enter the total units consumed: "))
bill = calculate_bill(units)
print(f"Your electricity bill is: Rs. {bill}")
>>>>>>> 8f8b0e4 (Add 1_python.py)
