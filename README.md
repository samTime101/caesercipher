## CaeserCipher in Python

I have used strings rather than converting strings to ASCII
I felt it easier
```py
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


```
