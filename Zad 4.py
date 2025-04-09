def trigger_index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"Zlapano wyjatek IndexError: {e}")

def trigger_zero_division_error():
    try:
        x = 10
        y = 0
        result = x/y
    except ZeroDivisionError as e:
        print(f"Zlapano wyjatel ZeroDivisionError: {e}")

def trigger_name_error():
    try:
        print(non_existent_variable)
    except NameError as e:
        print(f"Zlapano wyjatek NameErrdo: {e}")


trigger_index_error()
trigger_zero_division_error()
trigger_name_error()

print("Program kontynuuje dzialanie po obsludze wyjatkow.")