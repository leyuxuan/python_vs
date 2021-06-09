x = True
while x != 'q':
    x = input('加密（1）还是解密（2）？输入q退出:')
    def jia_mi():
        message = input("Enter a message to encode or decode: ") # Get a message
        message = message.upper()           # Make it all UPPERCASE :)
        output = ""                         # Create an empty string to hold output
        for letter in message:              # Loop through each letter of the message
            value = ord(letter) + 13    # shift the letter value up by 13,
            letter = value      # turn the value back into a letter,
        output += str(letter)                # Add the letter to our output string
        print("Output message: ", output)   # Output our coded/decoded message

    def jie_mi():
        message = input("Enter a message to encode or decode: ") # Get a message
        message = message.upper()           # Make it all UPPERCASE :)
        output = ""         # Create an empty string to hold output
        value = letter - 13
        for letter in message:              # Loop through each letter of the message
            letter = chr(value)         # turn the value back into a letter,
            output += letter                # Add the letter to our output string
        print("Output message: ", output)   # Output our coded/decoded message
    if x == '1':
        jia_mi()
    else:
        jie_mi()
