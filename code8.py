       #"""Word Reverser"""

#Input a sentence:
sentence = input("Enter a sentence: ")
#split each word ny given sentence:
words = sentence.split()
#for loop :
for word in words:
   print(word[::-1], end = " ")   #reverse each words in sentence:



