from tkinter import *
import pyautogui
from tkinter import messagebox as tmsg
import string
import random


eg = string.ascii_uppercase
print(eg)


root = Tk()
root.geometry("1000x550")
root.title("Hangman")


#images
hangman0 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman0.png")
hangman1 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman1.png")
hangman2 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman2.png")
hangman3 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman3.png")
hangman4 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman4.png")
hangman5 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman5.png")
hangman6 = PhotoImage(file = "C://Users//Carl//Desktop//Hangman//images//images//hangman6.png")

lst = [hangman0,hangman1,hangman2,hangman3,hangman4,hangman5,hangman6]

chances = Label(root,image = hangman0)
chances.grid(row = 0,column = 0)

#functioning of code

word = 'DEVELOPMENT' #you could create a list of words and append any random word

random_word = [x for x in word]
print(random_word)

check_word = ["?" for x in range(len(word))]


#choice for user
sample = []
for i in random_word:
	sample.append(i)

for i in range(5):
	sample.insert(random.randint(0,10),random.choice(eg))


word_label = Label(root,text = check_word,font= ("comicsans",50,"bold"))
word_label.grid(row=0,column=1)


num = 1

def hi():
	global num
	temp =check_alp.get()
	if len(temp) >1 :
		tmsg.showerror("Error","Only single Alphabet is required")
	elif temp == "":
		tmsg.showerror("Error","Please provide an Alphabet")
	else:
		if temp.capitalize() in random_word:
			ind = random_word.index(temp.capitalize())
			check_word.pop(ind)
			check_word.insert(ind,temp.capitalize())
			#print(check_word)
			word_label.configure(text=check_word)
			response = Label(text= "  Right Guess   ",font= ("comicsans",40,"bold"),fg= "green")
			response.grid(row=4,columnspan=2)
			if "?" not in check_word:
				tmsg.showinfo("Congragulations","      You win       ")

		else :
			try:
				response = Label(text= "Wrong Guess",font= ("comicsans",40,"bold"),fg= "red")
				response.grid(row=4,columnspan=2)
				chances.configure(image= lst[num])
				num+=1
			except IndexError:
				tmsg.showerror("You lose","Sorry, chances over")

	alp.set("")
	


Button(text = "CHECK",command = hi,height= 2,bg = "yellow").grid(row =2)


Label(text= "   Type an Alphabet:",font= ("comicsans",40,"bold")).grid(row=3,columnspan=2)

alp = StringVar()
check_alp = Entry(root,bg= "cyan",textvariable = alp)
check_alp.grid(row=3,column= 3)

Label(text= "CHOICES :"+str(sample),font= ("comicsans",20,"bold")).grid(row=5,columnspan=2)
 

root.mainloop()
