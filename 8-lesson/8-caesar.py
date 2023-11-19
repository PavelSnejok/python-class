# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(text, shift):
#     encrypt_text = ""
#     len_alphabet = len(alphabet)
#     for word in text:
#         current_index = alphabet.index(word) + shift
#         if current_index > len_alphabet - 1:
#             current_index -= len_alphabet
#             encrypt_text += alphabet[current_index]
#         else:
#             encrypt_text += alphabet[current_index]
#     print(encrypt_text)
#
# def decrypt(text, shift):
#     decrypted_text = ""
#     len_alphabet = len(alphabet)
#     for word in text:
#         current_index = alphabet.index(word) - shift
#         if current_index < 0:
#             current_index += len(alphabet)
#             decrypted_text += alphabet[current_index]
#         else:
#             decrypted_text += alphabet[current_index]
#     print(decrypted_text)
#
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("exit")

################################
import importlib

file_import_logo = importlib.import_module("8-logo")
logo = file_import_logo.logo
print(logo)


def caesar_encode_decode(direction, text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    if direction not in ["encode", "decode"]:
        print("chose a right direction!")
        return

    if direction == "decode":
        shift *= -1

    len_alphabet = len(alphabet)
    plain_text = ""
    shift %= len_alphabet

    for word in text:
        if word not in alphabet:
            plain_text += word
            continue
        current_index = alphabet.index(word) + shift
        if current_index > len_alphabet - 1:
            current_index -= len_alphabet
        elif current_index < 0:
            current_index += len_alphabet
        plain_text += alphabet[current_index]
    print(f"The {direction} text is {plain_text}\n")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_encode_decode(direction, text, shift)
    question = input("Do you want continue? Yes or No ").lower()
    if question == "no":
        should_continue = False
        print("Goodbye!!!")
