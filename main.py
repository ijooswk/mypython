def inputword():
    """This function get the word from the user and check if it's English word"""  
    word = input("Enter a word: ")
    if word.isalpha() == False:
        print("Error: Please enter only English letters")
        return inputword()
    else:
        return word
    
def checkword(word):
    """This function check if the word is in the dictionary"""
    with open("words.txt", "r") as file:
        for line in file:
            if word == line.strip():
                return True
        return False
    
def main():
    """This function get the word from the user and check if it's English word"""
    word = inputword()
    if checkword(word) == True:
        print("The word is in the dictionary")
    else:
        print("The word is not in the dictionary")

main()