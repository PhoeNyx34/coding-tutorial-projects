alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    message = ""

    for character in text:
        if character in alphabet:
            shifted_character = ""
            if direction == 'decode':
                shifted_character = alphabet.index(character) - (shift % 26) + 26
            else:
                shifted_character = alphabet.index(character) + (shift % 26)
            new_character = alphabet[shifted_character]

        if not character in alphabet:
                new_character = character
        
        message += new_character

    print(f"The resulting text is: {message}")

caesar(text,shift,direction)
