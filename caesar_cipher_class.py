
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
