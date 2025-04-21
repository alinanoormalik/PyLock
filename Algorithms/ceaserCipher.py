letters = 'abcdefghijklmnopqrstuvwxyz'

num_letters = len (letters)                           #input doesnt exceed limit

def encrypt_decrypt(text,mode,key): 
    result = ''
    if mode == 'd':
        key = -key                                    #as for decryption key moves in reverse direction

    for letter in text:
        letter = letter.lower()                       #if uer enters capital letters covert it
        if not letter == ' ' :
            index = letters.find(letter)              #find the index of letter entered by user
            if index == -1:                           #if letter not found
               result += letter                       
            else:
                new_index = index + key              #for output (encrypt will add directly and decrypt will perform -key)
                if new_index >= num_letters:         #wrapping for encryption
                    new_index -= num_letters         #for reverse
                elif new_index < 0 :                 #wrapping for decryption
                    new_index += num_letters
                result += letters [new_index]
        else:
            result += ' '                            #Add space back
    return result 




print()
print('**** CEASER CIPHER PROGRAM ****')
print()
print('Do you want to encrypt or decrypt?')
user_input= input('e/d: '). lower()                  #if user enters E OR D
print()

if user_input == 'e' :
   print('ENCRYPTION MODE SELECTED')
   print()
   key = int(input('Enter the key(1 through 26):'))  #user enters number and we shift according to that in the alphabets
   text = input('Enterr the text to encrypt: ')
   ciphertext=encrypt_decrypt(text,user_input,key)
   print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
     print('DECRYPTION MODE SELECTED')
     print()
     key = int(input('Enter the key(1 through 26):'))   
     text = input('Enter the text to decrypt: ')
     plaintext=encrypt_decrypt(text,user_input,key)
     print(f'PLAINTEXT: {plaintext}')

else:
    print("Invalid input. Please enter 'e' for encryption or 'd' for decryption")

