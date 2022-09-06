#CS 10 Python lab practice
import turtle as t
import string



#Simple String munipulation
def rev_string1(string): #This is a iteration
	a=""
	for i in list(string):
		a=i+a
	return a

def rev_string2(string):  #This is a recursion
	if len(string)==0:
		return ""
	else:
		return rev_string2(string[1:])+string[0]

def pig_latin(word):
	"""returns the pig latin translation of a word"""
	vowels=["a","e","i","o","u"]
	for x in range(0,len(word)):
		if word[x] in vowels:
			temp=word[0:x]
			return word[x:] + temp + "ay"
	return word + "ay"

def izzle(word):
    """ Returns the izzle translation of a word. """
    words=word.split()#turn the string into list of word
    vowels=["a","e","i","o","u"]
    def single_izzle(i):
    	for x in range(len(i)-1,-1,-1):#count from the last character in the word to the front
    		if i[x] in vowels:
    			return i[0:x] + "izzle"
    return ' '.join([single_izzle(i) for i in words])#list comprehension + turn list into string

def apply_language_game(text, language_game):
    """Takes a text and a language_game function as inputs"""
    """ Returns the language game function applied to every word of the text. """
    return language_game(text)

def count_words(text):
	"""Takes a text and returns a dictionary mapping each word to its count, for example:

	count_words(["Fruits and Vegetables and Vegetables on a Budget and Vegetables at a Store and Vegetables to Clean Fruit and Vegetables"])
	would return: 
	{'and': 5, 'on': 1, 'Vegetables': 5, 'Budget': 1, 'to': 1, 'Fruit': 1, 'a': 2, 'Clean': 1, 'Fruits': 1, 'Store': 1, 'at': 1}
	"""
	lst = remove_punctuation(text).split()#Trun depunctuated string into list
	dic={}

	for x in set(lst):
		dic[x]=0

	for i in lst:
			dic[i] += 1

	return dic.items()

def remove_punctuation(text):
    #method 1: lambda expression to delete punctuation
  	text1=map(lambda x: str.replace(x,string.punctuation,""),text)

  	#method 2: string comprehension(Problem: it returns a result twice)
  	text1=print([text.replace(x,"") for x in text if x in string.punctuation])


#dictionary
def top_n_words(counts, n,boring):
    """Returns the top n words by count without boring words. For example:
    top_n_words({'and': 5, 'on': 1, 'Vegetables': 5, 'Budget': 1, 'to': 1, 'Fruit': 1, 'a': 2, 'Clean': 1, 'Fruits': 1, 'Store': 1, 'at': 1}, 2)
    would return ["and", "Vegetables"].
    In the case of a tie, it doesn't matter which words are chosen to break the tie."""

    values=sorted(counts.values(),reverse=True)[:n]
    select=[]

    for i in values:
    	for x in counts.keys():
    		if i == counts[x]:
    			select.append(x)
    			del counts[x]#delete the key from dictionary to avoid being chosen twice
    			break#Once we find one key with the value we wanted , jump out of the loop in order to prevent that we select keys with the same value twice.


    for key in select:
    	print(key+counts[key])

def average_word_length(counts):
    """Returns the average length of a text with given counts. For example:

    average_word_length({'and': 5, 'on': 1, 'Vegetables': 5, 'Budget': 1, 'to': 1, 'Fruit': 1, 'a': 2, 'Clean': 1, 'Fruits': 1, 'Store': 1, 'at': 1}, 2)

    would return 5.0. This is because:
    Total letters: 3*5 + 2*1 + 10*5 + 6*1 + 2*1 + 5*1 + 1*2 + 5*1 + 6*1 + 5*1 + 2*1 = 100
    Total words: 5 + 1 + 5 + 1 + 1 + 1 + 2 + 1 + 1 + 1 + 1 = 20"""

    word_num=sum(list(counts.values()))
    letter_num=0
    for key in list(counts.keys()):
    	letter_num = letter_num + len(key) * counts[key]

    return letter_num / word_num

def word_diversity(counts):
	repeated_len=sum(list(counts.values()))
	unrepeated_len=len(list(counts.keys()))
	return unrepeated_len / repeated_len

#Marcov Chain Word Grnerator

	def get_kgram(text, ptr, k):
		"""Returns the kgram starting at position ptr in a text. For example:

		get_kgram("hello", 0, 3) would return "hel"
		get_kgram("hello", 1, 3) would return "ell"
		get_kgram("hello", 1, 4) would return "ello"
		get_kgram("hello", 3, 4) would crash since 3 + 4 is longer than the string."""
		if ptr + k > len(text):
			return ptr + k + "is longer than the string"
		else:
			return text[ptr:ptr+k]

	def process_character(m, text, ptr, k):
		"""Adds information about the given character to the model

		m is the model (a dictionary)
		text is the text
		text[ptr] is the character to be processed
		k is the order of our Markov chain"""
		pro_dic={}
		pro_dic[text[k+ptr]]=1
		m[get_kgram(text, ptr, k)]=pro_dic

	def build_markov_model(text, k):
		#Returns the markov model for text.
		#m is the model (a dictionary)
		#text is the text
		#k is the order of our Markov chain
		m={}
		for ptr in range(0,len(text)-k):
			if get_kgram(text, ptr, k) in m.keys():
				m[get_kgram(text, ptr, k)][text[ptr+k]] += 1
			else:
				process_character(m, text, ptr, k)
		return m


	def next_character_frequency(m, kgram, c):
		""" Returns the number of times c follows kgram
		m is the model (a dictionary)
		kgram is a kgram in in m
		c is a character that follows the given kgram"""
		return m[kgram][c]

def base_freq(string):
    original={"A":0,"T":0,"C":0,"G":0}
    for i in string:
        if i=="A":
            original["A"]+=1
        elif i=="T":
            original["T"]+=1
        elif i=="C":
            original["C"]+=1
        else:
            original["G"]+=1
    return original

def invert_dict(original):
    altered={}
    orig_key=list(original.keys())
    orig_value=list(original.values())
    for i in range(0,len(orig_key)):
        altered[orig_value[i]]=orig_key[i]
    return altered

def most_common(list):
    classify=dict()
    for i in list:
        if i not in np.array(classify.keys()):
            classify[i]=1
        else:
            classify[i] = classify[i] + 1

    max_num = max(np.array(classify.values()))
    
    common_list=[]
    
    for j in np.array(classify.keys()):
        if classify[j] == max_num:
            common_list.append(j)
    
    
    return common_list




#OOP
#See in other files in the folder



#list & list comprehension
def push_first_odd_back(lst):
    for i in range(0,len(lst)):
        if lst[i] % 2 == 1:
            temp=lst[i]
            lst.pop(i) 
            #pop and append do not need to be assigned to the list to save the changes
            lst.append(temp) 
            #also lst.insert(len(lst),temp) [insert puts a value in front of the input index]
            return lst
    return lst #if there is no odd number in the input list, return the original list

def flatten(lst):

    x=[]
    for i in lst:
        x=x+i  #"+" can be used to combine both string and list
    return x

def squares_of_evens(lst):
    return [x*x for x in lst if x%2==0]

def nth_power_of_evens(lst, n):
    return [x**n for x in lst if x%2==0]

def substitute_base(string, old, new):
    new_str=[]
    for letter in string:
        if letter==old:
            letter=new
        new_str.append(letter)

    return "".join(new_str)  #Turns the list new_str into a string


#Recurion & Loop

# C-Curve Turtle recursion
	def starter():
		t.setposition(0,0)
		t.heading()
		t.clear()
		t.pendown()

	def C_Curve(len,level):

		if level==1:
			t.forward(len)
		else:
			t.left(45)
			C_Curve(len*(1/2**0.5),level-1)
			t.right(90)
			C_Curve(len*(1/2**0.5),level-1)
			t.left(45)

def combine(lst):
    x=lst[0]
    for i in lst[1:]:
        x=x+i
    return x

def combine(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return(lst[0]+combine(lst[1:]))








