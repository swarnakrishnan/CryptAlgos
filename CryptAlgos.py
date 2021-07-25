from tkinter import *
import random
import webbrowser
from tkinter import ttk
from time import strftime
from ciphers import caesarCipher, homophonicCipher, railfenceCipher, autokeyCipher, atbashCipher, beaufortCipher, vignereCipher, vignereautokeyCipher, playfairCipher

root = Tk()
root.configure(background = 'midnight blue')
root.geometry('1000x600+100+50')
root.title("CryptAlgos")

# ----------------- Global strings ------------#

appName = "CryptAlgos"
labelName = "This is a Cryptography based application, useful for encrypting and decrypting \
of a text."
sideLabel = "To know more about cryptography"
downLabel = "Cryptography is the practice and study of techniques for \
secure communication in the presence of third parties called adversaries."
url = "https://en.wikipedia.org/wiki/Cryptography"

# ----------------- Partition -------------------#

left_pane = Frame(root, width = 200, height = 600, relief = RAISED)
left_pane.pack(side = LEFT)

main_frame = Frame(root, width = 800, height = 50, relief = RAISED, borderwidth = 10)
main_frame.pack()

main = Frame(root, width = 800, height = 400, relief = RAISED, bg = 'midnight blue')
main.pack()

main_label = Label(main, text = labelName, fg = "cyan",
	font = ('fixedsys', 18), anchor = CENTER, pady = 60)
main_label.grid(row = 0, column = 0, columnspan = 2)

label = Label(main_frame, text = appName, bg = "maroon", fg = "lemon chiffon",
	 bd = 10, font = ('fixedsys', 24, 'bold'), wraplength = 450, anchor = CENTER, padx = 20, pady = 20)

canvas = Canvas(left_pane)
frame = Frame(canvas)
myscrollbar = Scrollbar(left_pane, orient = VERTICAL, command = canvas.yview)
canvas.configure(yscrollcommand = myscrollbar.set)

def myfunction(event):
    canvas.configure(scrollregion = canvas.bbox("all"), width = 200, height = 600)

myscrollbar.pack(side = RIGHT, fill = Y)
canvas.pack(side = LEFT)
canvas.create_window((0,0), window = frame, anchor = NW)
frame.bind("<Configure>", myfunction)

sideLabelName = Label(main, text = sideLabel, fg = "gold", bg = 'midnight blue',
	font = ('fixedsys', 18), anchor = CENTER, wraplength = 200)
sideLabelName.grid(row = 0, column = 2)

downLabelName = Label(main, text = downLabel, fg = "gold", bg = 'midnight blue',
	font = ('fixedsys', 18), anchor = CENTER, wraplength = 500)
downLabelName.grid(row = 1, column = 0)

Exit = Button(main, text = "Exit", bd = 10, width = 10, command = root.destroy,  
	bg = 'maroon', fg = "lemon chiffon", font = ('arial', 12, 'bold'))
Exit.grid(row = 2, column = 1, columnspan = 2)

def show():

	remove()

	label.config(text = appName, bg = "maroon", fg = "lemon chiffon")
	label.grid(row = 0, column = 0)

	main_label = Label(main, text = labelName, font = ('fixedsys', 18), bg = 'midnight blue',
		anchor = CENTER, wraplength = 450, padx = 30, pady = 30, fg = "gold")
	main_label.grid(row = 0, column = 0, columnspan = 2)

	sideLabelName = Label(main, text = sideLabel, font = ('fixedsys', 18), 
		fg = "gold", anchor = CENTER, wraplength = 200, bg = 'midnight blue')
	sideLabelName.grid(row = 0, column = 2)

	downLabelName = Label(main, text = downLabel, fg = "gold", bg = 'midnight blue',
		font = ('fixedsys', 18), anchor = CENTER, wraplength = 500)
	downLabelName.grid(row = 1, column = 0)

	clickHere = Button(main, text = "Click Here", bd = 10, width = 10, activebackground = "black", fg = "lemon chiffon",
		command = openWiki, bg = 'maroon', font = ('arial', 12, 'bold'), activeforeground = "lemon chiffon")
	clickHere.grid(row = 0, column = 2, rowspan= 6)

	Exit = Button(main, text = "Exit", bd = 10, width = 10, command = root.destroy, activebackground = "black",
		bg = 'maroon', fg = "lemon chiffon", font = ('arial', 12, 'bold'), activeforeground = "lemon chiffon")
	Exit.grid(row = 1, column = 1, columnspan = 2)


def openWiki():
	webbrowser.open(url)

clickHere = Button(main, text = "Click Here", bd = 10, width = 10, 
	command = openWiki, bg = 'maroon', fg = "lemon chiffon", font = ('arial', 12, 'bold'))
clickHere.grid(row = 0, column = 2, rowspan= 6)

def remove():

	label.config(text = "")
	for widget in main.winfo_children():
		widget.destroy()

def lab():

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 16, "bold"), bg = "midnight blue", fg = "cyan")
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set, bg = 'gold')
	text_box.grid(row = 1, column = 0, pady = 1, padx = 1)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key: ", font = ('fixedsys', 14), pady = 15,
		bg = 'midnight blue', fg = "cyan")
	key_label.grid(row = 2, column = 0)	

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set, bg = 'gold')
	new_text.grid(row = 1, column = 2, columnspan = 2, padx = (10,0))
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')
	return text_box, new_text

def caesar_cipher():

	remove()

	label.config(text = "Caesar Cipher")
	label.grid(row = 0, column = 0)

	list_key = ttk.Combobox(main)
	list_key['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
	list_key.current(0)
	list_key.grid(row = 5, column = 0)

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nnumerical value 1-26\nDefault: 1"
	new_text.insert(1.0, sample)

	def encrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = int(list_key.get())
		enc_text = caesarCipher.encryption(txt, key)
		new_text.insert(1.0, enc_text)


	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 30)

	def decrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = int(list_key.get())
		dec_text = caesarCipher.decryption(txt, key)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)


def homophonic_cipher():

	remove()
	label.config(text = "Homophonic Cipher")
	label.grid(row = 0, column = 0)

	key_table = {'A':'D9', 'B':'X', 'C':'S', 'D':'F', 'E':'Z721', 'F':'E', 'G':'H', 'H':'C', 'I':'V3',
	'J':'I', 'K':'T', 'L':'P', 'M':'G', 'N':'A5', 'O':'Q0', 'P':'L', 'Q':'K', 'R':'J', 'S':'R4', 'T':'6U', 
	'U':'O', 'V':'W', 'W':'M', 'X':'Y', 'Y':'B', 'Z':'N', 'a':'d(', 'b':'x', 'c': 's', 'd':'f', 'e':'z&@!', 
	'f':'e', 'g':'h', 'h':'c', 'i':'v#', 'j':'i', 'k':'t', 'l':'p', 'm':'g', 'n':'a%', 'o':'q)', 'p':'l', 
	'q':'k', 'r':'j','s':'r$', 't':'^u', 'u':'o', 'v':'w', 'w':'m', 'x':'y', 'y':'b', 'z':'n'}

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'), bg = 'midnight blue', fg = "cyan")
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text.set, bg = 'gold')
	text_box.grid(row = 1, column = 0, pady = 1, padx = 1)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text2.set, bg = 'gold')
	new_text.grid(row = 1, column = 2, columnspan = 2, padx = (10,0))
	sample = "Sample text input:\nAny character\n"
	new_text.insert(1.0, sample)

	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		enc_text = homophonicCipher.encryption(txt)
		new_text.insert(1.0, enc_text)
    	
	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 20)

	def decrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		dec_text = homophonicCipher.decryption(txt)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)


def vignere_cipher():

	remove()
	label.config(text = "Vignere Cipher")
	label.grid(row = 0, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: a"
	new_text.insert(1.0, sample)

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = vignereCipher.encrypt(txt, key)
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 30)

	def decrypt():
	
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = vignereCipher.decrypt(txt, key)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	


def autokey_cipher():

	remove()
	label.config(text = "Autokey Cipher")
	label.grid(row = 0, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault: A"
	new_text.insert(1.0, sample)

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = autokeyCipher.encrypt(txt, key)
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 30)

	def decrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = autokeyCipher.decrypt(txt, key)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	


def railfence_cipher():

	remove()
	label.config(text = "Railfence Cipher")
	label.grid(row = 0, column = 0)

	list_key = ttk.Combobox(main)
	list_key['values'] = (2, 3, 4, 5, 6, 7, 8)
	list_key.current(0)
	list_key.grid(row = 5, column = 0)

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nPositive integer < length of input\nDefault: 2"
	new_text.insert(1.0, sample)

	def encrypt():

		new_text.delete('1.0', END)
		string = (text_box.get("1.0", END)).strip()
		key = int(list_key.get())
		enc_text = railfenceCipher.encrypt(string, key)
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 30)

	def decrypt():

		new_text.delete('1.0', END)
		string = (text_box.get("1.0", END)).strip()
		key = int(list_key.get())
		dec_text = railfenceCipher.decrypt(string, key)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	



def playfair_cipher():
	
	remove()
	label.config(text = "Playfair Cipher")
	label.grid(row = 0, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault: ABCD\n(Note:Case of key & text should be same)"
	new_text.insert(1.0, sample)


	def encrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = playfairCipher.encrypt(txt, key)
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 30)

	def decrypt(): 
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = playfairCipher.decrypt(txt, key)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	


def atbash_cipher():
	
	remove()
	label.config(text = "Atbash Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'), bg = 'midnight blue', fg = "cyan")
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text.set, bg = 'gold')
	text_box.grid(row = 1, column = 0, pady = 1, padx = 1)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')	

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text2.set, bg = 'gold')
	new_text.grid(row = 1, column = 2, columnspan = 2, padx = (10,0))
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')
	sample = "Sample text input:\nAny character\n"
	new_text.insert(1.0, sample)

	def convert():
		new_text.delete('1.0', END)
		string = text_box.get("1.0", END)
		converted_text = atbashCipher.encrypt(string)
		new_text.insert(1.0, converted_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = convert,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = convert,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 20)



def vignere_autokey_cipher():

	remove()
	label.config(text = "Vignere Autokey Cipher")
	label.grid(row = 0, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: a"
	new_text.insert(1.0, sample)

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = vignereautokeyCipher.encrypt(txt, key)
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 30)

	def decrypt():
	
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = vignereautokeyCipher.decrypt(txt, key)
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	


def beaufort_cipher():

	remove()
	label.config(text = "Beaufort Cipher")
	label.grid(row = 0, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	text_box, new_text = lab()
	sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: abc"
	new_text.insert(1.0, sample)

	def convert():
		spl = ['!','@','#','$','%','^','&','*','(',')','<','~',':',';','<','>','?','/']
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		converted_text = beaufortCipher.convert(txt, key)
		new_text.insert(1.0, converted_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = convert,
		bg = 'tomato2', fg = 'white')
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = convert,
		bg = 'tomato2', fg = 'white')
	dec.grid(row = 0, column = 3, padx = 10, pady = 30)	



# ----------------- Home Screen -------------------#

show()

# ----------------- Pane buttons -------------------#

home_button = Button(frame, padx = 20, bd = 10, text = 'Home', width = 20, height = 3, 
	command = show, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
home_button.grid(row = 0, column = 0)

caesar = Button(frame, padx = 20, bd = 10, text = 'Caesar Cipher', width = 20, height = 3, 
	command = caesar_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
caesar.grid(row = 1, column = 0)

homophonic = Button(frame, padx = 20, bd = 10, text = 'Homophonic Cipher', width = 20, height = 3, 
	command = homophonic_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
homophonic.grid(row = 2, column = 0)

vignere = Button(frame, padx = 20, bd = 10, text = 'Vignere Cipher', width = 20, height = 3, 
	command = vignere_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
vignere.grid(row = 3, column = 0)

autokey = Button(frame, padx = 20, bd = 10, text = 'Autokey Cipher', width = 20, height = 3, 
	command = autokey_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
autokey.grid(row = 4, column = 0)

railfence = Button(frame, padx = 20, bd = 10, text = 'Railfence Cipher', width = 20, height = 3, 
	command = railfence_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
railfence.grid(row = 5, column = 0)

playfair = Button(frame, padx = 20, bd = 10, text = 'Playfair Cipher', width = 20, height = 3, 
	command = playfair_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
playfair.grid(row = 6, column = 0)

atbash = Button(frame, padx = 20, bd = 10, text = 'Atbash Cipher', width = 20, height = 3, 
	command = atbash_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
atbash.grid(row = 7, column = 0)

vignere_autokey = Button(frame, padx = 20, bd = 10, text = 'Vignere Autokey Cipher', width = 20, height = 3, 
	command = vignere_autokey_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
vignere_autokey.grid(row = 8, column = 0)

beaufort = Button(frame, padx = 20, bd = 10, text = 'Beaufort Cipher', width = 20, height = 3, 
	command = beaufort_cipher, bg = 'PeachPuff3', fg = 'maroon', activebackground = 'red4', activeforeground = 'SeaGreen1')
beaufort.grid(row = 9, column = 0)

# C1 = Button(frame, padx = 20, bd = 10, text = 'Cipher', width = 20, height = 3)
# C1.grid(row = 13, column = 0)

root.mainloop()
