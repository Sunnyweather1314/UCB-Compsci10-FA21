from types import NotImplementedType
import numpy as np

# Spring 2018 
    """
    Write	a	function	that	returns	a	list of	the most common	elements in	a sequence. You	must use	a	dictionary	
    in	your	solution;	if	you	forget	any	commands,	remember	there"s	help(type)and	 dir(type),	as	in	
    help(dict) or	dir(str). You may find the min and max functions helpful.

    example 1:
    most_common([1,2,3,3,4,4,6,4,4,5,5,5,5])
    >>> [4, 5]


    exmaple 2:
    most_common("uc berkeley also cal")
    >>> ["l", " ", "e"]

    """

    #way 1 def most_common(sequence):
    def most_common(list):
        classify={}
        for i in list:
            if i not in classify.keys():
                classify[i]=1
            else:
                classify[i] = classify[i] + 1
        
        max_num = max(classify.values())
        
        common_list=[]
        
        for j in classify.keys():
            if classify[j] == max_num:
                common_list.append(j)
        
        return common_list

    #way 2 def most_common(sequence):
    def most_common(list):
        counts = {}
        for elem in list:
            if elem in counts:
                counts[elem] += 1
            else:
                counts[elem] = 1
                
        max_val = max(counts.values())
        return [elem for elem in counts if counts[elem] == max_val]
        #uses list comprehension instead of using another for loop, which gives the lines less space complexity

    most_common([1,2,3,3,4,4,6,4,4,5,5,5,5])
    most_common("uc berkeley also cal")



# Spring 2018

    """
    Write a function that returns the longest list of unique words that start with the same letter given any
    string of lower-case words. You must use a dictionary in your solution; if you forget any commands,
    remember there"s help(type)and dir(type), as in help(dict) or dir(str). If a word is repeated
    in a string, you should not include that word again. In the case of a tie, you may return any of lists that
    correspond to the letters that have the most words in that string. In other words, if there were an equal
    number of words that start with "s" and "t", you can return either the list of words that start with "s" or the
    list of words that start with "t". You may find the min and max functions helpful.

    example1:
    starts_with_same_letter("to be or not to be that is the question")
    >>> ["to", "that", "the"]

    example2:
    starts_with_same_letter("been there believe that")
    >>> ["been", "believe"]

    """
    # method 1 (for loop)
        def starts_with_same_letter1(sentence):
            word_list = sentence.split()
            starter = dict()
            
            for word in word_list:
                if word[0] not in starter.keys():
                    starter[word[0]] =set([word])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                else:
                    starter[word[0]].add(word)                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            max_len = max([len(j) for j in starter.values()])
            
            for j in starter.keys():
                if len(starter[j]) == max_len:
                    return starter[j]
                
            
    # method 2 (usage of lambda and max function)
        def starts_with_same_letter2(sentence):
            word_list = sentence.split()
            starter = dict()
            
            for word in word_list:
                if word[0] not in starter.keys():
                    starter[word[0]] =set([word])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                else:
                    starter[word[0]].add(word)  
                    
            return max(starter.values() , key = lambda lst : len(lst))

# Fall 2018

    """
    Write	a	function	that	find_GC that	takes	in	two	dictionaries	(GP capturing	grandparentsàparents,	and	
    PC capturing	parentsàchildren)	and	returns	a	new	dictionary	of	all	grandparentsàchildren it	finds. As	an	
    example,	we	have	three	grandparents:	1,	2	and	3;	three	parents:	10,	11	and	12;	and	two	children:	100	and	
    200 with	à connections	as	shown	below.	Your	function	would	return	the two grandparentsàchildren:	
    1à100 and 2à100. By	the	way, more	than	2	grandparents	can	à to the	same	parent;	similarly	for	
    parentsàchildren (sometimes	family	records	get	corrupted,	it's not	our	job	to	worry	about	that).

    explaination page: http://cs10.org/sp20/exams/in-lab-final/2018Fa/exam.pdf

    example:
    GP = {1:10, 2:10, 3:11}
    PC = {10:100, 12:200}
    find_GC(GP,PC)

    >>> {1: 100, 2: 100}

    """


    def find_GC(GP , PC):
        GC = dict()
        for i in GP:
            if GP[i] in PC:
                GC[i] = PC[GP[i]]
        return GC


#Spring 2019
    """
    We	want to	know which TAs had at least half of	their discussions full.	We have	two	dictionaries:

    • enrollment: represents the	number	of	students enrolled in each discussion
    o Key: TA name	
    o Value: # of enrolled students

    • attendance: represents the attendance	for	each discussion
    o Key: TA name	
    o Value: list representing the number of students that attended	that discussion each week

    Assume	we	had	10	discussions. Write the function	TAs_with_at_least_half_discussions_full, that
    returns	a list of the names of TAs who had at least	half (i.e.,	≥ 5) of	their discussions full.
    (We	underline the full discussions for each TA,	and	the	TAs	with at	least half of them full below.)

    pdf instruction: http://cs10.org/sp20/exams/in-lab-final/2019Sp/exam.pdf


    example:
    sp19_enrollment = {"Murtaza": 10, "Lara": 20, "Mansi":20, "Niki":15, "Brendan": 10}
    sp19_attendance = {"Murtaza": [10, 9, 10, 10, 10, 2, 9, 10, 9, 1],
                        "Lara": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                        "Mansi": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25],
                        "Niki": [20, 15, 15, 12, 17, 17, 17, 16, 18, 20],
                        "Brendan": [ 5, 5, 4, 2, 3, 10, 11, 12, 4, 2] }
                        
    >>> TAs_with_at_least_half_discussions_full(sp19_enrollment, sp19_attendance)
    >>> ['Murtaza', 'Mansi', 'Niki']

    """

    # method 1
        def TAs_with_at_least_half_discussions_full(enrollment , attendance):
            check_half = dict()
            
            for i in enrollment:
                check_half[i] = np.count_nonzero([ j >= enrollment[i] for j in attendance[i]]) / len(attendance[i])
                
            above_half = list()
            
            for x in check_half:
                if  check_half[x] >= 0.5:
                    above_half.append(x)
                    
            return above_half

    #method 2
        def TAs_with_at_least_half_discussions_full(enrollment, attendance):
            TAs = []
            for TA in attendance:
                num_full = len([x for x in attendance[TA] if x >= enrollment[TA]])
                if num_full >= 5:
                    TAs.append(TA)
            return TAs


# Spring 2020
    """

    Write Python code for this problem and put it in the YourfirstnameYourlastname.py file.
    Your friend Bif creates a new sequence that starts with 1, 2, and 3. After that, the next value is
    the sum of the previous three values. The first five values are 1, 2, 3, 6, 11, as shown below:

    Sequence number Sequence
    1 1
    2 2
    3 3
    4 6 (the sum of 1,2, and 3)
    5 11 (the sum of 2, 3, and 6)
    ... ...

    In python, write a function bif_dict(N) that takes a sequence number N returns a dictionary (for
    all the numbers 1 through N inclusive) whose keys are the sequence number and values are the
    sequence. You should be able to call bif_dict(100)and have it return very quickly.


    example:
    >>> bif_dict(5)
    >>> {3: 3, 2: 2, 1: 1, 4: 6, 5: 11}

    answers:https://drive.google.com/file/d/1yEzOB_eSSu4HC_RSUsx7ei77j66dhCeY/view

    """



    # method 1(tRYING RECURSION BUT NOT WORKING)
        def bif_dict(n):
            if n == 1:
                return {1:1}
            if n < 4 :
                
                return {1:1 , 2:2 , 3:3}
            else:
                a = bif_dict[n-1] + bif_dict[n-2] + bif_dict[n-3]
                bif_dict(n-1)[n] = a
                return 

    # method 2 (for loop)
        def bif_dict2(N):
            ret_dict = {1:1, 2:2, 3:3}
            last_three = [1,2,3]
            
            for i in range(4, N+1):
                sum_last_three = sum(last_three)
                ret_dict[i] = sum_last_three
                last_three = last_three[1:] + [sum_last_three]
                
            return ret_dict
        
    # method 3
        """Simillar thought process as method 2"""
        def bif_dict(N):
            d = {1: 1, 2: 2, 3: 3}
            x = 1
            y = 2
            z = 3
            for i in range(4, N + 1):
                e = x + y + z
                d[i] = e
                x, y, z = y, z, e
            return d

    # method 4 
        """calculate a single number and then add them up together"""
        def bif_single(n):
            if n < 4:
                return n
            else: 
                return bif_single(n-1) + bif_single(n-2) + bif_single(n-3)
            
            
        def bif_dict3(n):
            D = dict()
            
            for i in range(1 , n+1):
            D[i] = bif_single(i) 
            
            return D
                    
    # method 5
        D = {}

        def bif(n):
            if n in D:
                return D[n]
            elif n < 4:
                D[n] = n
                return n
            else:
                D[n] = bif(n-1)+bif(n-2)+bif(n-3)
                return D[n]

        def bif_dict(n):
            bif(n)
            return D

    # method 6
    def bif_dict(n):
        ans = {}
        for i in range(1, 4):
            ans[i] = i
        for i in range(4, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]
        return ans


#writing quiz

#summer 2018 final
    def compound_word(word , single_word):
        """
        For the purposes of this question, let's define a compound word as a word composed exclusively of
        two simple words. A simple word is any word that cannot be broken into two smaller words. For
        example, “blackboard” is a compound word because it consists of exactly two simple words: “black”
        and “board.” “Computer,” on the other hand, is a simple word.
        
        example:
        simple_words = [“basket”, “base”, “ball”]
        >>> compound_word(“basketball”, simple_words)
        True
        
        """
        
        word1 = ""
        index = 0
        for letter in word:
            word1 += letter
            if word1 in single_word:
                if word[index:] in single_word or compound_word(word[index:] , single_word):
                    return True
            index += 1
        return False

# Summer 2019 final
    #>>> my_list = [1, 2]
    #>>> repeat_seven(my_list)
    #>>> [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]

    def repeat_seven(input_list):
        return [input_list for i in range(7)]

#fall 2021

    #method 1
        def total_points(scores):
            return sum(list(map(lambda x , y : x if y-x < 10 and y > x else 0 , [i[0] for i in scores] , [j[1] for j in scores])))

    #method 2
    def total_points2(scores):
        return sum([scores[i][0] if scores[i][1]-scores[i][0]<10 and scores[i][1]-scores[i][0]>0 else 0 for i in range(len(scores))])

    print(total_points2([[100,5],[80,81],[50,40],[3,30],[60,70],[91,90],[19,10],[20,29]]))