def is_valid_credit_card(number):
    num_str = str(number)
    length = len(num_str)
    

    if length < 13 or length > 16:
        return False
    if not (num_str.startswith('4') and length == 13 or
            num_str.startswith('5') and length == 13 or
            num_str.startswith('37') and length == 16 or
            num_str.startswith('6') and length == 15):
        return False

    total = 0
    for i in range(length - 1, -1, -1):
        digit = int(num_str[i])
        if (length - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit = digit // 10 + digit % 10
        total += digit
    
    return total % 10 == 0


while True:
    try:
        card_number = int(input("Enter a credit card number or 0 to exit : "))
        if card_number == 0:
            break
        if is_valid_credit_card(card_number):
            print("Valid credit card number")
        else:
            print("Invalid credit card number")
    except ValueError:
        print("Please enter a valid integer")

print("Program ended.")