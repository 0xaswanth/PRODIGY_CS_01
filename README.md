
# Caesar Cipher Program - Prodigy InfoTech Internship Task 1

## Objective
This Python program implements the **Caesar Cipher algorithm**, which allows users to encrypt and decrypt text using a shift value. The program provides a simple menu interface where users can select between encryption and decryption.

## Technologies Used
- **Python 3.x**
- **Object-Oriented Programming (OOP)**

## Features
- **Encryption:** Encrypts a message by shifting the letters by a user-defined value.
- **Decryption:** Decrypts an encrypted message using the correct shift value.
- **Menu-driven Interface:** A simple text-based menu for selecting encryption, decryption, or exiting the program.

## Instructions
1. Clone this repository to your local machine.
2. Run the Python script using Python 3.x.
3. The program will present a menu with options to either **Encrypt**, **Decrypt**, or **Exit**.
4. Enter the message and shift value as prompted to see the encrypted or decrypted result.

## How to Run
To run the program, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Aswanthkp333/PRODIGY_CS_01.git
    cd PRODIGY_CS_01
    ```

2. Execute the Python script:
    ```bash
    python caesar_cipher.py
    ```

3. Select an option from the menu and follow the prompts to either encrypt or decrypt a message.

## Sample Output

### Encrypting a Message:
```
Choose an option (1/2/3): 1
Enter your message: Hello World!
Enter shift number: 3
Encrypted Message: Khoor Zruog!
```

### Decrypting a Message:
```
Choose an option (1/2/3): 2
Enter your message: Khoor Zruog!
Enter shift number: 3
Decrypted Message: Hello World!
```

## Code Overview

```python
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def process(self, text, mode):
        result = ''
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                if mode == 'encrypt':
                    shifted = (ord(char) - base + self.shift) % 26
                else:
                    shifted = (ord(char) - base - self.shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        return result

def main():
    print("==== Caesar Cipher Tool ====")
    while True:
        print("
Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1' or choice == '2':
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter shift number: "))
            except ValueError:
                print("Shift must be a number.")
                continue

            cipher = CaesarCipher(shift)
            if choice == '1':
                output = cipher.process(message, 'encrypt')
                print("Encrypted Message:", output)
            else:
                output = cipher.process(message, 'decrypt')
                print("Decrypted Message:", output)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
```

## Acknowledgments
- **Prodigy InfoTech** for the opportunity to work on this task.
