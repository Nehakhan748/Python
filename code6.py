          #"""Vowel Counter"""

#Input a sentence:
sentence = input("Enter a sentence: ")
#taking lowercase sentence:
sentence = sentence.lower()
vowals_list = ["a", "e", "i", "o", "u"]
vowal_count = 0               #Initilize vowal_count zero:
#Use for loop to find vowals in sentence:
for char in sentence:        
    if char in vowals_list:    #Char used to find the same characters from senetnce & vowal_list:
       vowal_count += 1
print("Total Vowal",vowal_count)


