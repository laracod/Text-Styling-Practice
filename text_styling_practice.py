"""
Features:
Uppercase version
Lowercase version
Reversed text
Vowel count
Consonant count
Number of words
Remove all spaces
Check if it is a palindrome (same forwards & backwards)
"""


user_text = None


def menu():
    global user_text
    print("##############################")
    print("This is a string styling tool!")
    print("##############################")
    user_text = str(input("Enter your text: "))


def upper(u_text):
    #u_text.upper()
    return u_text.upper()

def lower(u_text):
    #u_text.lower()
    return u_text.lower()

def reverse(u_text):
    reversed_text = ""
    for letter in range(len(u_text) - 1, -1, -1):
        reversed_text = reversed_text + u_text[letter]
    return reversed_text

def vowel_count(u_text):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter_num in range(len(u_text)):
        letter = u_text[letter_num]
        for vowel in vowels:
            if letter == vowel:
                count += 1
    return count

def consonant_count(u_text):
    count = 0
    consonants = ["b", "c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z",
                  "B","C","D","F", "G", "H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
    for letter_num in range(len(u_text)):
        letter = u_text[letter_num]
        for consonant in consonants:
            if letter == consonant:
                count += 1
    return count

def num_of_words(u_text):
    count = 0
    in_word = False
    for letter_num in range(len(u_text)):
        letter = u_text[letter_num]

        # entering a new word
        if not letter.isspace() and in_word == False:
            count += 1
            in_word = True
        # leaving a word
        elif letter.isspace():
            in_word = False
    return count

def remove_all_spaces(u_text):
    new_word = ""
    for letter_num in range(len(u_text)):
        letter = u_text[letter_num]
        if not letter.isspace():
            new_word += letter
    return new_word

def palindrome_check(u_text):
    backwards = u_text[::-1]
    if u_text == backwards:
        palindrome = True
    else:
        palindrome = False
    return palindrome

#'''
def summary():
    global user_text
    print("##############################")
    print("           SUMMARY            ")
    print("##############################")
    print("\n")
    print(f"Uppercase: {upper(user_text)}")
    print(f"Lowercase: {lower(user_text)}")
    print(f"Reversed: {reverse(user_text)}")
    print(f"Number of vowels: {vowel_count(user_text)}")
    print(f"Number of consonants: {consonant_count(user_text)}")
    print(f"Number of words: {num_of_words(user_text)}")
    print(f"All spaces removed: {remove_all_spaces(user_text)}")
    print(f"Palindrome?: {palindrome_check(user_text)}")
#'''

on = True
while on == True:
    menu()
    summary()
    user_input = input("Would you like to enter another word?")
    if user_input.lower() == "y":
        on = True
    else:
        on = False
        break



