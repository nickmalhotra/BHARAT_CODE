from Hindi import *
from Marathi import *
from Odia import *
from Gujarati import *
from Telugu import *
from Kannada import *
from Punjabi import *
from Malayalam import *
from Maori import *

class Language_Factory():

	def call_language(self,lang):
		lang_dict = {"Hindi": Hindi,"Marathi":Marathi,"Odia":Odia,"Gujarati":Gujarati,
					 "Telugu":Telugu,"Kannada":Kannada,"Punjabi":Punjabi,"Malayalam":Malayalam,
					 "Maori":Maori} 
		target_class = lang.capitalize()
		return lang_dict[target_class]()