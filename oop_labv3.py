class Book:
	def __init__(self, genre, title, author, py):
		self.genre=genre
		self.title=title
		self.author=author
		self.publication_year=py


		
	def calculate_age(self):
		#Calculates the age of the book by subtracting its publication year from the current year.
		return 2021-self.publication_year

	def outdated(self, old_age):
		#Determines if the book is outdated. Takes in an old_age and return True or False.
		#Should return True if the age is at least old_age
		if self.calculate_age() <= old_age:
			return False
		else:
			return True


	genres = {}

	def add_genre(self):
		'''If the book's genre isn't in the genres, then you'll need to add the genre to genres
		as well as the original book's information. Otherwise, just make sure the book isn't
		inside genres before you add it!'''

		if self.genre not in Book.genres.keys():
			Book.genres[self.genre]=[self.title,self.author]
		else: 
			Book.genres[self.genre].append([self.title,self.author])
		return Book.genres


class MooingBook(Book):    
    def moo(self):
        print("On behalf of " + self.author +  ", I moo.")



class MemePage:

	def __init__(self, topic):
		self.topic=topic
		self.posts={}		
		self.members=0




class Member:

	actvity=0
	num_posts=0


	def __init__(self, name, memepage):# no quotation marks needed for memepage attribute
		self.name=name
		self.memepage=memepage
		memepage.members = memepage.members + 1


	def tag_ur_friend_in_meme(self, friend, title_of_post):

		if title_of_post not in self.memepage:
			return "You cannot tag someone in a meme if they are not a member of this page."
		else:
			self.actvity=self.activity + 1

			return "@"+ friend + "has been tagged!"


	def post_in_page(self, title_of_post):

		if title_of_post in self.title_of_post:
			return "You have been banned for reposting a meme."
		else:
			self.actvity=self.activity + 1
			self.memepage.posts.append(title_of_post)
			self.memepage.posts[title_of_post]=len(self.memepage.posts)
			return "Your total activity on this " + self.memepage.topic + " page is " + self.actvity + ", and your total posts to it is now" + len(self.memepage.posts[title_of_post]) + " is "


	def like_a_post_in_page(self, title_of_post):
		self.activity += 1
		self.memepage.posts[title_of_post] += 1
		return "Your total activity on this " + self.memepage.topic + " page is " + self.actvity + ", and the total number of likes on the post" + title_of_post + " is " + self.memepage.posts[title_of_post]
