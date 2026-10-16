import secrets
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(secrets.choice(characters) for _ in range(length))

    return password


while True:
    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than zero!")
            continue

    except ValueError:
        print("Please enter a valid number!")
        continue

    letters = input("Include letters? (yes/no): ").strip().lower() == "yes"
    numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

    password = generate_password(length, letters, numbers, symbols)

    if password is None:
        print("Please select at least one character type!")
        continue

    print("\nYour generated password is:", password)

    save_choice = input("Do you want to save this password? (yes/no): ").strip().lower()

    if save_choice == "yes":
        try:
            with open("passwords.txt", "a") as file:
                file.write(password + "\n")

            print("Password saved successfully!")

        except OSError:
            print("Error: Could not save the password!")

    again = input("Generate another password? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for using Password Generator!")
        break