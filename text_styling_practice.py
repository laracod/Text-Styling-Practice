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
    text.upper(u_text)
    return u_text

def lower(u_text):
    text.lower(u_text)
    return(u_text)

def reverse(u_text):
    for letter in range(len(u_text) - 1, -1, -1):
        reversed_text = reversed_text + u_text[letter]
    return(reversed_text)

def vowel_count(u_text):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter_num in range(len(u_text)):
        letter = u_text[letter_num]
        for vowel in vowels:
            if letter == vowel:
                count += 1
    return(count)

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

    
menu()
print(consonant_count(user_text))


