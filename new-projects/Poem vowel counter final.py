Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  #This will be the list of characters that we're searching for total.
Lowercase_vowel = ['a', 'e', 'i', 'o', 'u']    # I've broken them up in to two groups upper and lower case.
Uppercase_vowel = ['A', 'E', 'I', 'O', 'U']    # I've broken them up in to two groups upper and lower case.


Lowercase_count = 0                            #Initiate Counter for Lowercase vowels start from zero.
Uppercase_count = 0                            #Initiate Counter for Uppercase vowels start from zero.
Vowel_count = 0                                #Initiate Counter for Vowels total start from zero.


Poem = input("Enter a poem or text to count the number of vowels: \n\n")    #This lets the user input some text 
                                                                                        #(a sequence of letters).


for letter in Poem:                            #I'm using a for loop to iterate over the sequence of letters.
    if letter in Vowel:                                  #If letter is a vowel, it will be counted.
        Vowel_count += 1                                 #Every time we find an vowel the count rises by 1.
    if letter in Lowercase_vowel:                        #If letter is a lowercase vowel, it will be counted.
        Lowercase_count += 1                             #Every time we find a lowercase vowel the count rises by 1.
    if letter in Uppercase_vowel:                        #If letter is a upperercase vowel, it will be counted
        Uppercase_count += 1                             #Every time we find an uppercase vowel the count rises by 1.      
              
print("\nThere are", Vowel_count, "vowels in total")       #Print will then send result of Vowel_count to the console.
print("\nThere are", Lowercase_count, "lowercase vowels")  #Print will then send result of lowercase_count to the console.
print("\nThere are", Uppercase_count, "uppercase vowels")  #Print will then send result of Upperrcase_count to the console.

#I decided to keep the 3 counters, as a check against my upper and lowercase totals.
#Also I like the input method to enter the poem. This means that the program will be useful for other poems and texts too!