# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import font
import xml.etree.ElementTree as ET 
from ttkthemes import ThemedTk 
from Language_Factory import *

# Everything in Tkinter is a widget, so let us create a root widget.This has to happen before 


#Defines a cluster of buttons and total buttons in a line
CLUSTER = 6
TOTAL_IN_A_LINE = 40
base_language = "hindi"


root = Tk()
root.title('BHARAT CODE - HTML EDITOR FOR INDIC LANGUAGE')
root.geometry('1500x800')

#Global variable kept for the BHAML tags 
bml_tags = []


'''Make 3 frames in the window. Frame 1 , the biggest one for coding.Frame 2, for html support and 
frame 3 for buttons that would evolve'''
#Create the three frames need for the IDE
bharat_frame = Frame(root)
bharat_frame.place(height=500, width=1000, x=0, y=0)

bottom_frame = Frame(root)
bottom_frame.place(height=300, width=1000, x=0, y=500)
bottom_frame.config(bg='orange')

side_frame = Frame(root)
side_frame.place(height=800, width=500, x=1000, y=0)

#Setting the Language as a default one and providing an ability to change it.
lang = Language_Factory()



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

	#Delete previous text
	my_text.delete("1.0",END)

	#Grab file name 
	text_file = filedialog.askopenfilename(initialdir="./",title="Open File",
				filetypes=(("BHAML Files","*.bhaml"),("All files","*.*")))
	#Update statuses
	name = text_file
	root.title(f'{name} - Bharat Code!')

	#Open file
	with open(text_file,'r',encoding='utf8') as f:
		file_data = f.read()

	#Add file to textbox
	my_text.insert(END,file_data)


#Create an save as file function
def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="./",title="Save File",
											 filetypes=(("BHAML Files","*.bhaml"),("All files","*.*")))

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

			final_html_text = final_text

			#Step 4. If the file extension is "BHAML, then open again and rewrite the html construct"
			if str(file_extension).lower() == "bhaml":
				
				print("BHAML Text Found....\n")
				#print("The base language is " +base_language)
				tags_array = read_bharat_xml(base_language)

				for i in range(len(tags_array)): 
					split_tags = str(tags_array[i]).split("!#@")
					#print(split_tags)
					lang_tag = split_tags[-1].replace("]","")
					lang_tag = lang_tag.replace("'","")
					html_eng_tag = split_tags[0].replace("[","")
					if(final_html_text.find(lang_tag) > -1): 
						#print("Found Hindi tag:\t" + hindi_tag+"\n")
						#print("Found english tag:\t" + html_eng_tag+"\n")
						final_html_text = final_html_text.replace(lang_tag , html_eng_tag)

				with open(file_name+'.html','w', encoding='utf-8') as f:
					f.write(final_html_text)


def alpha_click(my_text,alpha):
	my_text.insert(INSERT,alpha)


def create_language_widgets(base_language):
	#Getting buttons made in a specific language and placing them in the bottom widget by a loop 

	obj = lang.call_language(base_language)
	button_strings = obj.button_strings()
	BASE_X = 0
	BASE_Y = 0
	counter=0
	button_arr = []

	if button_strings: #If button strings exist
		if len(button_strings) > 0:
			for i in range(len(button_strings)):
				BASE_X = counter*20
				
				if (counter)%(TOTAL_IN_A_LINE)==0:
					#Add 40 pixels to Y Point keep a distance between button
					BASE_X = 0
					BASE_Y = BASE_Y + 40
					counter = 0
				counter = counter+1	
				button_arr.append(Button(bottom_frame,text=button_strings[i],command=lambda alpha=button_strings[i]: alpha_click(my_text,alpha)))
				button_arr[i].config(bg='white',fg='black',relief=RAISED,highlightcolor='blue')
				button_arr[i].place(x=BASE_X+30,y=BASE_Y)
	

def create_base_widget(base_language):
	#Create our scrollbar for the bharat code frame and side frame
	scroll_bharat=Scrollbar(bharat_frame, orient='vertical')
	scroll_bharat.pack(side=RIGHT,fill=Y)

	scroll_side=Scrollbar(side_frame,orient='vertical')
	scroll_side.pack(side=RIGHT,fill=Y)


	#Create a text widget
	my_text = Text(bharat_frame,
				  font=("Consolas",12),selectbackground="gray",selectforeground="black",
				  undo=True,yscrollcommand=scroll_bharat.set)
	#my_text.place(x=0,y=0,width=1100,height=700)
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

	#Configure our scrollbar for side frame
	scroll_side.config(command=my_text_right.yview)


	#Call to create button widgets for the language and place them in bottom frame
	create_language_widgets(base_language)

	return my_text_right,my_text

def change_language(lang):
	#Change global variable of base language to changed language
	global base_language
	base_language = lang
	title = 'BHARAT CODE - Language Changed-' + base_language.capitalize()
	format_system_for_language(my_text,title,my_text_right,base_language)

def create_menu(root):
	#Create Menu
	my_menu = Menu(root)
	root.config(menu=my_menu)

	#Add file menu 
	file_menu = Menu(my_menu,tearoff=False)
	my_menu.add_cascade(label="File" , menu=file_menu)
	file_menu.add_command(label="New", command=new_file)
	file_menu.add_command(label="Open", command=open_file)
	file_menu.add_command(label="Save")
	file_menu.add_command(label="Save As", command=save_as_file )
	file_menu.add_separator()
	file_menu.add_command(label="Exit",command=root.quit)

	#Add edit menu
	edit_menu = Menu(my_menu,tearoff=False)
	my_menu.add_cascade(label="Edit" , menu=edit_menu)
	edit_menu.add_command(label="Cut")
	edit_menu.add_command(label="Copy")
	edit_menu.add_command(label="Undo")
	edit_menu.add_command(label="Redo")
	#edit_menu.add_command(label="Change Language")

	#Add Menus to Change language
	lang_menu = Menu(my_menu,tearoff=False)
	my_menu.add_cascade(label="Change Language" , menu=lang_menu)
	lang_menu.add_command(label="हिंदी - Hindi", command=lambda:change_language('hindi'))
	lang_menu.add_command(label="मराठी - Marathi", command=lambda:change_language('marathi'))
	lang_menu.add_command(label="ଓଡିଆ - Odia", command=lambda:change_language('odia'))
	lang_menu.add_command(label="தமிழ் - Tamil", command=lambda:change_language('tamil'))
	lang_menu.add_command(label="বাংলা - Bangla", command=lambda:change_language('bangla'))
	lang_menu.add_command(label="ગુજરાતી - Gujarati", command=lambda:change_language('gujarati'))
	lang_menu.add_command(label="తెలుగు - Telugu", command=lambda:change_language('telugu'))
	lang_menu.add_command(label="ಕನ್ನಡ - Kannada", command=lambda:change_language('kannada'))
	lang_menu.add_command(label="ਪੰਜਾਬੀ - Punjabi", command=lambda:change_language('punjabi'))
	lang_menu.add_command(label="മല്യാലം - Malayalam", command=lambda:change_language('malayalam'))

	return my_menu,file_menu,edit_menu,lang_menu

def format_text(my_text_right,tags_array):
	my_text_right.insert(INSERT,"QUICK SUMMARY OF TAGS\n")
	for i in range(len(tags_array)):
		split_tags = str(tags_array[i]).split("!#@")
		my_text_right.insert(INSERT,"HTML TAG:" + split_tags[1].replace("[","") + "\n")
		my_text_right.insert(INSERT,"USAGE:" + split_tags[2] + "\n")
		my_text_right.insert(INSERT,"BHAML TAG:" + split_tags[-1].replace("]","") + "\n")
		my_text_right.insert(INSERT,'................................................\n')

def read_bharat_xml(language):
	# Reading the data inside the xml file to a variable under the name data 
	tree = ET.parse('bharat.xml') 
	root = tree.getroot()
	#print("Reading XML for..." + language)
	bml_tags=[]
	for tags in root.findall('BML'):
		elements=""
		elements = tags.find('name').text + "!#@" + tags.find('normal_usage').text + "!#@" +tags.find('description').text + "!#@"+tags.find(language).text
		bml_tags.append(elements)

	return bml_tags

my_text_right,my_text = create_base_widget(base_language)
my_menu,file_menu,edit_menu,lang_menu = create_menu(root)

tags_array = read_bharat_xml(base_language)
format_text(my_text_right,tags_array)


#Create a main loop for root widget
root.mainloop()