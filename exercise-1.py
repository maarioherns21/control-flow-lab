# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
letter = input(" Please enter a letter from the alphabet (a-z or A-Z)").lower()

while letter != "quit":
# 2. Write the code that determines whether the letter entered is a vowel
    if letter in "'a','e','i','o','u'":
        print(f"the letter {letter} is vowel ")

    # 3. Print one of following messages (substituting the letter for x):
    #      - The letter x is a vowel
    elif letter == "x":
        print(f"the letter {letter} is a consanant as well")
    #      - The letter x is a consonant
    else:
        print("is not a vowel!")
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
    letter = input(" Please enter a letter from the alphabet (a-z or A-Z)").lower()
