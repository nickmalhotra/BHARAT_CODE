from Hindi import *
from Marathi import *
from Odia import *

class Language_Factory():

	def call_language(self,lang):
		lang_dict = {"Hindi": Hindi,"Marathi":Marathi,"Odia":Odia} 
		target_class = lang.capitalize()
		return lang_dict[target_class]()