'''
The Python Bible, Zyad Yehia, Project 7, Pig latin translator,  
Student: Lukasz

Pig Latin, words examples:

consonants as a start letter:

    happy -> appyHay
    pig -> igPay
    duck -> ucsDay
    glove -> oveGlay

if vowels as a start letter:

    apple = appleyay
    eat -> eatyay

'''

# consonants:
# if second letter is vowel word without first letter plus upper
# first letter plus ay
#if second letter is consonant, word wotiout two first letters plus
# upper first, lower second plus ay

#vowels:
# word plus yay

print("PiG LatiN TranslatoR")
print()


print()


# interface using while loop (functions: translation, exit program,
# info about not exisdting finctions
while True:  

    i = input("What would you like to do? 1 - translate, 2 - exit").strip()

    if i == '1':

# input the sentence to translate
        translated_sentence = input("What would you like to translate?").strip().lower()          

        trans_list = translated_sentence.strip("?").strip(".").strip(",").strip(":").split(" ") #exclude punctation marks or spaces

# list with the preliminary result
        new_list = [] 

# loop and conditions to change a words in a proper way according to the
# piglatin
        for word in trans_list: 
               
            if word[0] in 'aeiou':
                word = word.lower() + 'yay'
                new_list.append(word)
            else:
                vowel_pos = 0
                for letter in word:
                    if letter not in 'aeyiou':
                        vowel_pos += 1
                    else:
                        break
                cons = word[:vowel_pos]
                the_rest = word[vowel_pos:]
                new_word = the_rest + cons +'ay'
                new_list.append(new_word)

# exchange list on string
        result = " ".join(new_list)

# output the result      
        print("Here is your translation: ", result)

# exit progran 
    elif i == '2': 
        print("Goodyay yebay!")
        break
    
#informing that function different than 1 or 2 does not exists.
    else: 
        print("This function does not exist. Choose the number from 1 to 2")
