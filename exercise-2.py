# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
words = input ('Enter a phrase: ').lower()
print(f" Your word or phrase is : {words}")

while words != "quit":
# 2. Print the following message:
    if words == words:
        print('What you entered is '+ str(len(words)) + ' characters long')
    else:
        print('Not found')
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
    words = input ('Enter a phrase: ').lower()