# -*- coding: utf-8 -*-
import re
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox 
import xml.etree.ElementTree as ET 
from ttkthemes import ThemedStyle 
from Language_Factory import *


#Defines a cluster of buttons and total buttons in a line
CLUSTER = 6
TOTAL_IN_A_LINE = 30
global base_language
base_language = "hindi"

lang_dict = {"Hindi": Hindi,"Marathi":Marathi,"Odia":Odia,"Gujarati":Gujarati,
			 "Telugu":Telugu,"Kannada":Kannada,"Punjabi":Punjabi,"Malayalam":Malayalam} 


global selected 
selected = False

# Everything in Tkinter is a widget, so let us create a root widget.This has to happen before 
root = Tk()
root.title('BHAML - BHARAT MARK UP LANGUAGE EDITOR')
photo = PhotoImage(file = "images/india.png")
root.iconphoto(True, photo)
root.geometry('1500x800')

style= ThemedStyle(root)
style.set_theme('smog')


'''top = Toplevel()
filename = PhotoImage(file = "images/Bhaml_v2.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
top.geometry('800x600')
'''

#Global variable kept for the BHAML tags 
bml_tags = []


'''Make 3 frames in the window. Frame 1 , the biggest one for coding.Frame 2, for html support and 
frame 3 for buttons that would evolve'''
#Create the three frames need for the IDE
#bg = PhotoImage(file="./images/india.jpg")

bharat_frame = Frame(root)
bharat_frame.place(height=600, width=1000, x=0, y=0)
bharat_frame.config(bg='#030303')

bottom_frame = Frame(root)
bottom_frame.place(height=300, width=1000, x=0, y=500)
bottom_frame.config(bg='#C9542B')

side_frame = Frame(root)
side_frame.place(height=800, width=500, x=1000, y=0)

#Setting the Language as a default one and providing an ability to change it.
lang = Language_Factory()

#Set global variable for open file names
global open_status_name
open_status_name = False

#Function to change the formats as language is changed
def format_system_for_language(my_text,title,my_text_right,language):
	#Delete previous text in the editor
	my_text.delete("1.0",END)
	#Give a new title to the window
	root.title(title)
	my_text.pack(side=TOP,fill=X)
	#Call language factory to get base language
	obj = lang.call_language(language)
	base_file_text = obj.base_file_message()

	#Insert language text in the code editor
	my_text.insert(INSERT,base_file_text)

	#Format the right text bar as well while reading tags of that language
	my_text_right.delete("1.0",END)
	tags_array1 = read_bharat_xml(language)
	format_text(my_text_right,tags_array1)

	#Format language widgets as well in the bottom frame for the base language
	for widget in bottom_frame.winfo_children():
		widget.destroy()

	#Recreate widgets 
	create_language_widgets(language)

#Create new file function
def new_file():
	title = "BHARAT CODE - New File"
	format_system_for_language(my_text,title,my_text_right,base_language)

#Create an open file function
def open_file():


	#Grab file name 
	text_file = filedialog.askopenfilename(initialdir="./",title="Open File",
				filetypes=(("BHAML Files","*.bhaml"),("All files","*.*")))

	#Check to see if there is a file name and then make filename global to access it later
	if text_file:
		global open_status_name
		open_status_name = text_file

	#Update statuses
	name = text_file
	root.title(f'{name} - Bharat Code!')

	#try:
	#Open file
	with open(text_file,'r',encoding='utf8') as f:
		file_data = f.read()

		if file_data:
			#Delete previous text
			my_text.delete("1.0",END)
			#Add file to textbox
			my_text.insert(END,file_data)

			#Find Head in the tree 
			# Reading the data inside the xml file to a variable under the name head 
			### This is critical , as if you are in Hindi file format and you may open a file of a diff language###
			tree = ET.parse('bharat.xml') 
			tree_root = tree.getroot()
			for tags in tree_root.findall('BML'):
				if tags.find('name').text == 'head':
					for child in tags:
						if str(file_data).find(child.text) > -1:
							base_language = child.tag
							#print(child.tag, child.text)

			#Add text on the right for tags
			my_text_right.delete("1.0",END)
			tags_array1 = read_bharat_xml(base_language)
			format_text(my_text_right,tags_array1)

			#Format language widgets as well in the bottom frame for the base language
			for widget in bottom_frame.winfo_children():
				widget.destroy()

			#Recreate widgets 
			create_language_widgets(base_language)
		else:
			pass
	
	#except:
		#messagebox.showinfo("File Opening Info", "File not found!! Please choose a file to load") 

#Create a save file function
def save_file():
	global open_status_name
	global base_language 
	tags_array = []

	if open_status_name:
		with open(open_status_name,'w', encoding='utf8') as f:

			#Step 1. Get the text of the file
			final_text = my_text.get(1.0,END)

			#Look at the first line or ines in this file and determine language
			for key in lang_dict:
				#print(key)
				if str(key).lower() in final_text.lower():
					base_language = key
					

			#print("Base Language Found..." + base_language)

			#Step 2. Get the file extension
			file_splitted = open_status_name.split(".")
			file_name = file_splitted[0]
			file_extension = file_splitted[1]
			

			#Step 3. Write the file as it is to the disk
			f.write(final_text)

			final_html_text = final_text

			#Step 4. If the file extension is "BHAML, then open again and rewrite the html construct"
			if str(file_extension).lower() == "bhaml":
				
				#print("BHAML Text Found....\n")
				#print("The base language is " +base_language)
				tags_array = read_bharat_xml(base_language)

				for i in range(len(tags_array)): 
					split_tags = str(tags_array[i]).split("!#@")
					lang_tag = split_tags[-1].replace("]","")
					lang_tag = lang_tag.replace("'","")
					html_eng_tag = split_tags[0].replace("[","")
					
					if(final_html_text.find(lang_tag) > -1): 
						#print("Found Hindi tag:\t" + hindi_tag+"\n")
						#print("Found english tag:\t" + html_eng_tag+"\n")
						#NOW REPLACE TAGS
						index_of_bhaml_tag = final_html_text.find(lang_tag)
						
						#Get the full word
						lang_word =  str(final_html_text[index_of_bhaml_tag:index_of_bhaml_tag+len(lang_tag)])
						
						if(final_html_text[index_of_bhaml_tag-1] == "<" and final_html_text[index_of_bhaml_tag+len(lang_tag)] == ">"):
							#print("Pure tag found....replacing...")
							final_html_text = final_html_text.replace(lang_tag , html_eng_tag)
						elif(final_html_text[index_of_bhaml_tag-2] == "<" and final_html_text[index_of_bhaml_tag-1] == "/" and final_html_text[index_of_bhaml_tag+len(lang_tag)] == ">"):
							#print("Pure tag found....replacing...")
							final_html_text = final_html_text.replace(lang_tag , html_eng_tag)
						elif(final_html_text[index_of_bhaml_tag-1] == "<" ):
							if final_html_text[index_of_bhaml_tag+len(lang_tag)]==" ":					
								final_html_text = final_html_text.replace(lang_tag , html_eng_tag)

				with open(file_name+'.html','w', encoding='utf-8') as f:
					f.write(final_html_text)
			else:
				messagebox.showinfo("File Opening Info", "Please only load a .BHAML file") 
	else:
		save_as_file()

#Create an save as file function
def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="./",title="Save File",
											 filetypes=(("BHAML Files","*.bhaml"),("All files","*.*")))

	final_text = ""
	tags_array = []

	if text_file:
		name = text_file
		root.title(f'{name} - Bharat Code!') 

		with open(text_file,'w', encoding='utf8') as f:
			#Step 1. Get the text of the file
			final_text = my_text.get(1.0,END)

			#Step 2. Get the file extension
			file_splitted = text_file.split(".")
			file_name = file_splitted[0]
			file_extension = file_splitted[1]
			

			#Step 3. Write the file as it is to the disk
			f.write(final_text) 
			###############BHAML FILE SAVED HERE##################

			#Use final text now to save as HTML also
			final_html_text = final_text


			#Step 4. If the file extension is "BHAML, then open again and rewrite the html construct"
			if str(file_extension).lower() == "bhaml":
				
				#print("BHAML Text Found....\n")
				#print("The base language is " +base_language)
				tags_array = read_bharat_xml(base_language)

				# HTML tag replacement
				for i in range(len(tags_array)): 
					split_tags = str(tags_array[i]).split("!#@")
					lang_tag = split_tags[-1].replace("]","")
					lang_tag = lang_tag.replace("'","")
					html_eng_tag = split_tags[0].replace("[","")
					
					if(final_html_text.find(lang_tag) > -1): 
						#print("Found Hindi tag:\t" + hindi_tag+"\n")
						#print("Found english tag:\t" + html_eng_tag+"\n")
						#NOW REPLACE TAGS
						index_of_bhaml_tag = final_html_text.find(lang_tag)
						
						#Get the full word
						lang_word =  str(final_html_text[index_of_bhaml_tag:index_of_bhaml_tag+len(lang_tag)])
						
						if(final_html_text[index_of_bhaml_tag-1] == "<" and final_html_text[index_of_bhaml_tag+len(lang_tag)] == ">"):
							#print("Pure tag found....replacing...")
							final_html_text = final_html_text.replace(lang_tag , html_eng_tag)
						elif(final_html_text[index_of_bhaml_tag-2] == "<" and final_html_text[index_of_bhaml_tag-1] == "/" and final_html_text[index_of_bhaml_tag+len(lang_tag)] == ">"):
							#print("Pure tag found....replacing...")
							final_html_text = final_html_text.replace(lang_tag , html_eng_tag)
						elif(final_html_text[index_of_bhaml_tag-1] == "<" ):
							if final_html_text[index_of_bhaml_tag+len(lang_tag)]==" ":					
								final_html_text = final_html_text.replace(lang_tag , html_eng_tag)
						

				with open(file_name+'.html','w', encoding='utf-8') as f:
					f.write(final_html_text)
			else:
				messagebox.showinfo("File Opening Info", "Please only save as a .BHAML file") 


#Create a function to look at click of a button
def alpha_click(my_text,alpha):
	my_text.insert(INSERT,alpha)

#Create all language based widgets
def create_language_widgets(language):
	#Getting buttons made in a specific language and placing them in the bottom widget by a loop 
	global base_language 
	base_language = language

	obj = lang.call_language(base_language)
	button_strings = obj.button_strings()
	BASE_X = 0
	BASE_Y = 0
	counter=0
	button_arr = []

	lang_label = Label(bottom_frame,padx=10,text=base_language.upper()+" KEYBOARD")
	lang_label.config(bg='#C9542B',fg='black',highlightcolor='blue',width=40,height=2,font='bold')
	lang_label.place(x=BASE_X+300,y=BASE_Y)

	if button_strings: #If button strings exist
		if len(button_strings) > 0:
			for i in range(len(button_strings)):
				BASE_X = counter*30
				
				if (counter)%(TOTAL_IN_A_LINE)==0:
					#Add 40 pixels to Y Point keep a distance between button
					BASE_X = 0
					BASE_Y = BASE_Y + 40
					counter = 0
				counter = counter+1	
				button_arr.append(Button(bottom_frame,text=button_strings[i],command=lambda alpha=button_strings[i]: alpha_click(my_text,alpha)))
				button_arr[i].config(bg='white',fg='black',relief=RAISED,highlightcolor='blue',width=3,height=1)
				button_arr[i].place(x=BASE_X+30,y=BASE_Y)
	
#Function to create base widgets	
def create_base_widget(base_language):
	#Create our scrollbar for the bharat code frame and side frame
	scroll_bharat=Scrollbar(bharat_frame, orient='vertical')
	scroll_bharat.pack(side=RIGHT,fill=Y)

	scroll_side=Scrollbar(side_frame,orient='vertical')
	scroll_side.pack(side=RIGHT,fill=Y)


	#Create a text widget
	my_text = Text(bharat_frame,
				  font=("Consolas",12),selectbackground="gray",selectforeground="black",
				  undo=True,yscrollcommand=scroll_bharat.set, insertbackground='white')
	my_text.config(bg="#030303",fg="white")
	my_text.pack(side=TOP,fill=X)

	#Adjust its scroll bar
	scroll_bharat.config(command=my_text.yview)

	#Get Base language data based on selected language
	obj = lang.call_language(base_language)

	#Fill the text with base code for html in the language
	base_file_text = obj.base_file_message()
	my_text.insert(INSERT,base_file_text)


	#Create a text widget for the side frame, so that HTML tags can be shown
	my_text_right = Text(side_frame,
				  font=("Consolas",10),selectbackground="yellow",selectforeground="black",
				  undo=True,yscrollcommand=scroll_side.set)
	my_text_right.place(x=0,y=0,height=800,width=500)
	my_text_right.config(bg="gray",fg="white")
	#Configure our scrollbar for side frame
	scroll_side.config(command=my_text_right.yview)


	#Call to create button widgets for the language and place them in bottom frame
	create_language_widgets(base_language)

	return my_text_right,my_text

#CHange language function
def change_language(lang):
	#Change global variable of base language to changed language
	global base_language
	base_language = lang
	title = 'BHARAT CODE - Language Changed-' + base_language.capitalize()
	format_system_for_language(my_text,title,my_text_right,base_language)

def cut_text(e):
	global selected 
	#Check to see if keyboard shortcut was used and if there is something in the buffer
	if e:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			#Grab selected text from the text box
			selected = my_text.selection_get()
			#Delete the selection from the text box
			my_text.delete("sel.first","sel.last")
			# Clear the clipboard and append the selected text
			root.clipboard_clear()
			root.clipboard_append(selected)

def copy_text(e):
	global selected 
	#Check to see if keyboard shortcut was used and if there is something in the buffer
	if e:
		selected = root.clipboard_get()
	if my_text.selection_get():
		#Grab selected text from the text box
		selected = my_text.selection_get()
		# Clear the clipboard and append the selected text
		root.clipboard_clear()
		root.clipboard_append(selected)


def paste_text(e):
	global selected 
	#Check to see if keyboard shortcut was used and if there is something in the buffer
	if e:
		selected = root.clipboard_get()
	else:
		if selected:
			#Grab the position of the cursor
			position = my_text.index(INSERT)
			#Insert the text in the position
			my_text.insert(position,selected)

#Menu creation function
def create_menu(root):
	#Create Menu
	my_menu = Menu(root)
	root.config(menu=my_menu)

	#Add file menu 
	file_menu = Menu(my_menu,tearoff=False)
	my_menu.add_cascade(label="File" , menu=file_menu)
	file_menu.add_command(label="New", command=new_file)

	file_menu.add_command(label="Open", command=open_file)
	file_menu.add_command(label="Save", command=save_file)
	file_menu.add_command(label="Save As", command=save_as_file )
	file_menu.add_separator()
	file_menu.add_command(label="Exit",command=root.quit)

	#Add edit menu
	edit_menu = Menu(my_menu,tearoff=False)
	my_menu.add_cascade(label="Edit" , menu=edit_menu)
	edit_menu.add_command(label="Cut   Ctrl+x" ,command=lambda:cut_text(False))
	edit_menu.add_command(label="Copy  Ctrl+c",command=lambda:copy_text(False))
	edit_menu.add_command(label="Paste Ctrl+v",command=lambda:paste_text(False))
	#edit_menu.add_command(label="Change Language")

	#Add Menus to Change language
	lang_menu = Menu(my_menu,tearoff=False)
	my_menu.add_cascade(label="Change Language" , menu=lang_menu)
	lang_menu.add_command(label="हिंदी - Hindi", command=lambda:change_language('hindi'))
	lang_menu.add_command(label="मराठी - Marathi", command=lambda:change_language('marathi'))
	lang_menu.add_command(label="ଓଡିଆ - Odia", command=lambda:change_language('odia'))
	lang_menu.add_command(label="ગુજરાતી - Gujarati", command=lambda:change_language('gujarati'))
	lang_menu.add_command(label="తెలుగు - Telugu", command=lambda:change_language('telugu'))
	lang_menu.add_command(label="ಕನ್ನಡ - Kannada", command=lambda:change_language('kannada'))
	lang_menu.add_command(label="ਪੰਜਾਬੀ - Punjabi", command=lambda:change_language('punjabi'))
	lang_menu.add_command(label="മല്യാലം - Malayalam", command=lambda:change_language('malayalam'))

	return my_menu,file_menu,edit_menu,lang_menu

def format_text(my_text_right,tags_array):
	
	for i in range(len(tags_array)):
		split_tags = str(tags_array[i]).split("!#@")
		my_text_right.insert(INSERT,"HTML TAG:" + split_tags[1].replace("[","") + "\n")
		my_text_right.insert(INSERT,"USAGE:" + split_tags[2] + "\n")
		my_text_right.insert(INSERT,"BHAML TAG:" + split_tags[-1].replace("]","") + "\n")
		my_text_right.insert(INSERT,'................................................\n')

#Function to read BHAML 
def read_bharat_xml(language):
	global base_language
	base_language = language

	# Reading the data inside the xml file to a variable under the name data 
	tree = ET.parse('bharat.xml') 
	root = tree.getroot()

	#Empty the BML tags first
	bml_tags=[]
	try:
		my_text_right.insert(INSERT,"QUICK SUMMARY OF TAGS\n\n")
		for tags in root.findall('BML'):
			elements=""
			elements = tags.find('name').text + "!#@" + tags.find('normal_usage').text + "!#@" +tags.find('description').text + "!#@"+tags.find(base_language.lower()).text
			bml_tags.append(elements)
	except:
		my_text_right.delete(1.0,END)
		my_text_right.insert(INSERT,"HTML TAGS NOT READY AS YET\n\n")
	return bml_tags

my_text_right,my_text = create_base_widget(base_language)
my_menu,file_menu,edit_menu,lang_menu = create_menu(root)

tags_array = read_bharat_xml(base_language)
format_text(my_text_right,tags_array)

'''def find_text(e):
	if e: 
		#Grab the position of the cursor
		position = my_text.index(INSERT)
		#Insert the text in the position
		my_text.insert(position,'अ')
'''

#Edit Bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)

# To be used later
#root.bind('<Alt-Key-a>',find_text)

#Create a main loop for root widget
root.mainloop()