while True:
    try:
        num1 = float(input("Please write a number: "))
        num2 = float(input("Please write a number: "))
        product = num1 * num2
        if num1 != num2:
            print(num1, "*", num2, "=", product)
            break
        elif num1 == num2:
            print("You can't multiply the same numbers")
    except ValueError:
        print("Please write a number ")
