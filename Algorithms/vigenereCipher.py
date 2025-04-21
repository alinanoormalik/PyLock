def msg_and_key():
    # Takes user input and maps the key to match message length (ignoring spaces)
    print("Message and key can only be alphabetic")
    msg = input("Enter message: ").upper()
    key = input("Enter key: ").upper()

    key_map = ""                                                 # Holds the expanded key
    j = 0

    for i in range(len(msg)):
        if ord(msg[i]) == 32:
            key_map += " "                                       # Preserve spaces
        else:
            if j < len(key):
                key_map += key[j]                                # Use next key character
                j += 1
            else:
                j = 0                                            # Restart key from beginning
                key_map += key[j]
                j += 1

    return msg, key_map


def create_vigenere_table():
    # Creates the 26x26 Vigenère table used for encryption and decryption
    table = []
    for i in range(26):
        table.append([])                                          # Initialize each row

    for row in range(26):
        for column in range(26):
            if (row + 65) + column > 90:
                table[row].append(chr((row + 65) + column - 26))  # Wrap around after 'Z'
            else:
                table[row].append(chr((row + 65) + column))       # Add shifted letter

    return table


def cipher_encryption(message, mapped_key):
    # Encrypts the message using the mapped key and Vigenère table
    table = create_vigenere_table()
    encrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            encrypted_text += " "                                  # Preserve spaces
        else:
            row = ord(message[i]) - 65                             # Row from message letter
            column = ord(mapped_key[i]) - 65                       # Column from key letter
            encrypted_text += table[row][column]                   # Get encrypted letter

    print("Encrypted Message: {}".format(encrypted_text))


def itr_count(mapped_key, message):
    # Counts how many positions from key letter to encrypted letter (used in decryption)
    counter = 0
    result = ""

    for i in range(26):
        if mapped_key + i > 90:
            result += chr(mapped_key + (i - 26))                   # Wrap around after 'Z'
        else:
            result += chr(mapped_key + i)                          # Build shifted alphabet row

    for i in range(len(result)):
        if result[i] == chr(message):
            break                                                  # Found cipher letter
        else:
            counter += 1                                           # Count steps

    return counter


def cipher_decryption(message, mapped_key):
    # Decrypts the message using the mapped key and Vigenère logic
    table = create_vigenere_table()
    decrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            decrypted_text += " "                                  # Preserve spaces
        else:
            # Convert cipher letter back to plain letter using step count
            decrypted_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))

    print("Decrypted Message: {}".format(decrypted_text))


def main():
    # Main control function: lets user choose encryption or decryption
    print("** Vigenere Cipher **")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    
    if choice == 1:
        print("---Encryption---")
        message, mapped_key = msg_and_key()
        cipher_encryption(message, mapped_key)

    elif choice == 2:
        print("---Decryption---")
        message, mapped_key = msg_and_key()
        cipher_decryption(message, mapped_key)

    else:
        print("Wrong choice. Select 1 or 2")


if __name__ == "__main__":
       main()                                                         # Entry point of the program
   
