       #"""Word Length Filter"""

#Input a sentence:
sentence = input("Enter a sentnce: ")
words = sentence.split()      #Split the given sentence:
#for loop to print words(lenght greater than 4)
for word in words:
#use if statement 
   if len(word) > 4:
     print(word)
