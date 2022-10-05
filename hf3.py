def inputs():
    def division(a, b):
        return a / b

    while 0 < 1:
        a_value = int(input("Enter 'a' value: "))
        b_value = int(input("Enter 'b' value: "))

        try:
            print(division(a_value, b_value))

        except ZeroDivisionError:
            print("Division by zero not allowed")

        finally:
            print("Out of except blocks")


if __name__ == "__main__":
    inputs()
