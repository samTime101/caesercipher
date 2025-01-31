# SAMIP REGMI
# ADDED ON GITHUB JAN 29
# CAESER CIPHER COURSEWORK
# ** DOC STRINGS ADDED IN EACH FUNCTION FOR BETTER REDEABILITY **
import os
def welcome():
    '''
    parameter:No parameter
    returns : None
    prints welcome message
    '''
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text using Caesar Cipher.")
def enter_message():
    '''
    parameter: No parameter
    returns mode  , message , and shift 
    '''
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        print("Invalid Mode")
    message = input("What message would you like to process: ").strip().upper()
    while True:
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid Shift")
    return mode, message, shift

def encrypt(message, shift_number):
    '''
    parameter: message, shift_number
    returns : encrypted_result
    just encrypts the message
    '''
    total_possibilities = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_result = ''
    for character in message:
        index = total_possibilities.find(character.lower())
        if index == -1:
            encrypted_result += character
        else:
            output_index = (index + shift_number) % len(total_possibilities)
            encrypted_result += total_possibilities[output_index]
    return encrypted_result.upper()

def decrypt(message, shift_number):
    '''
    parameter: message, shift_number
    returns: decrypted_result
    just decrupts the message
    '''
    total_possibilities = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_result = ''
    for character in message:
        index = total_possibilities.find(character.lower())
        if index == -1:
            decrypted_result += character
        else:
            output_index = (index - shift_number) % len(total_possibilities)
            decrypted_result += total_possibilities[output_index]
    return decrypted_result.upper()


def is_file(filename):
    '''
    parameter:filename
    reuturns in boolean if the given file exists or not
    '''
    return os.path.isfile(filename)

def process_file(filename, mode):
    '''
    parameter: filename , mode
    returns: processed_messages
    processes the line , line by line
    '''
    if not is_file(filename):
        print(f"File '{filename}' does not exist.")
        return

    processed_messages = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if mode == 'e':
                processed_messages.append(encrypt(line, shift_number))
            elif mode == 'd':
                processed_messages.append(decrypt(line, shift_number))
    return processed_messages

def write_messages(messages):
    '''
    parameters:messages
    return: None
    writes messages in the file
    '''
    with open('./results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')
    print(f"Output written to results.txt")

def message_or_file():
    '''
    parameter:None
    return:None
    prompts user to choose console or read from file
    '''
    global shift_number
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode not in ['e', 'd']:
            print("Invalid Mode")
            continue

        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source == 'f':
            while True:
                filename = input("Enter a filename: ").strip()
                if is_file(filename):
                    break
                print("Invalid Filename")
            while True:
                try:
                    shift_number = int(input("What is the shift number: "))
                    if not (0 <= shift_number <= 25):
                        raise ValueError("Shift must be between 0 and 25")
                    break
                except ValueError:
                    print("Invalid Shift")
            return mode, None , filename
        elif source == 'c':
            message = input("What message would you like to process: ").strip().upper()
            while True:
                try:
                    shift_number = int(input("What is the shift number: "))
                    if not (0 <= shift_number <= 25):
                        raise ValueError("Shift must be between 0 and 25")
                    break
                except ValueError:
                    print("Invalid Shift")
            return mode, message, None
        else:
            print("Invalid input. Choose 'f' for file or 'c' for console.")

def main():
    '''
    main function of the program
    '''
    welcome()
    while True:
        mode, message, filename = message_or_file()
        
        if filename:
            messages = process_file(filename, mode)
            if messages:
                write_messages(messages)
        else:
            if mode == 'e':
                print(encrypt(message, shift_number))
            elif mode == 'd':
                print(decrypt(message, shift_number))
        
        while True:
            another = input("Would you like to encrypt or decrypt another message? (y/n): ").strip().lower()
            if another == 'y':
                break  
            elif another == 'n':
                print("Thanks for using the program, goodbye!")
                return  
            else:
                print('Invalid , please choose y or n')

if __name__ == "__main__":
    main()
