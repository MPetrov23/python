import random
import string


def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def enter_length():
    length = input("Enter the length of the password (minimum 6): ")
    try:
        length = int(length)
        if length < 6:
            print("Length must be at least 6!")
            return enter_length()
        else:
            return length
    except ValueError:
        print("Please enter a valid number!")
        return enter_length()


def main():
    print("Password Generator v1.0")
    while True:
        length = enter_length()
        password = generate_password(length)
        print(password)
        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another == "yes":
            continue
        elif another == "no":
            print("Goodbye!")
            quit()
        else:
            print("Invalid input!")
            quit()


if __name__ == '__main__':
    main()
