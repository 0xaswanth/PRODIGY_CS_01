# PRODIGY_CS_01
Cyber Security Internship Task for Prodigy InfoTech

Caesar Cipher Program - Prodigy InfoTech Internship Task 1
Objective
This Python program implements the Caesar Cipher algorithm, which allows users to encrypt and decrypt text using a shift value. The program supports both encryption and decryption operations, and users can provide their own message and shift value for the process.

Technologies Used
Python 3.x

OOP (Object-Oriented Programming)

Features
Encryption: The program takes a message and a shift value to encrypt the text.

Decryption: Users can also decrypt an encrypted message by providing the correct shift value.

Menu Interface: The program offers a simple text-based menu to select between encryption, decryption, or exiting the program.

Instructions
Clone this repository to your local machine.

Run the caesar_cipher.py file using Python 3.x.

You will be presented with a menu where you can choose to Encrypt, Decrypt, or Exit.

Enter the message you want to encrypt or decrypt.

Input the shift value (an integer).

The program will output the encrypted or decrypted message based on your choice.

How to Run
To run the program, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/Aswanthkp333/PRODIGY_CS_01.git
cd PRODIGY_CS_01
Execute the Python script:

bash
Copy
Edit
python caesar_cipher.py
Follow the on-screen instructions to select encryption or decryption options.

Example
Sample Input for Encryption:
pgsql
Copy
Edit
Choose an option (1/2/3): 1
Enter your message: Hello World!
Enter shift number: 3
Encrypted Message: Khoor Zruog!
Sample Input for Decryption:
yaml
Copy
Edit
Choose an option (1/2/3): 2
Enter your message: Khoor Zruog!
Enter shift number: 3
Decrypted Message: Hello World!
Code Overview
python
Copy
Edit
# Caesar Cipher Program - Version 2
# By Sneha KM

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
        print("\nMenu:")
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
Acknowledgments
Prodigy InfoTech for providing the opportunity to work on this internship task.

