class Gujarati(object):
	def __init__(self):
		self.language='Gujarati'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY (BHAML GUJARATI)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<ભમલ>"
		base_message += "\n\n\t<હેડ>"
		base_message += "\n\t\t<શીર્ષક>भारत कोड</શીર્ષક>"
		base_message += "\n\t<લિપિ ભાષા=""Javascript"">"
		base_message += "\n\n\t\tકાર્ય message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\tચેતવણી('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</લિપિ>"
		base_message += "\n\t</હેડ>"
		base_message += "\n\n\t<બોડી>"
		base_message += "\n\t\t<ફકરો>Hello there! mera naam Nikhil hai!</ફકરો>"
		base_message += "\n\t\t<એ ચરેફ=""http://www.google.com"">Google</એ>"
		base_message += "\n\t\t<ઇનપુટ પ્રકાર=બટન value='कलिक' onClick='message();'></ઇનપુટ>"
		base_message += "\n\t</બોડી>"
		base_message += "\n\n</ભમલ>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"ଅ"," ଆ","ା","ବ","ଭ","ଚ",
								"ଛ","କ୍ଷ","ଦ","ଧ","ଡ","ଢ",
								"ଦ୍ଧ","ଦ୍ଵ","ଦ୍ଯ","ଦ୍ଦ","ଦ୍ନ","ଦ୍ମ",
								"େ","ୈ","ଏ","ଐ ୖ","ଫ","ଗ",
								"ଘ","ଙ","ହ","ହ୍ମ","ହ୍ଯ","ହ୍ଲ",
								"ହ୍ନ","ହ୍ଵ","ି","ୀ","ଇ","ଈ",
								"ଜ","ଝ","ଯ","ଞ","ଜ୍ଞ","କ",
								"ଖ","କ୍ତ","ଲ","ଳ","ୢ","ଌ",
								"ୡ","ମ","ନ","ଣ","ୋ","ୌ",
								"ଓ","ଔ","ୗ","ପ","ର","୍ର",
								"ୃ","ର୍","ଡ଼୍","ଡ଼","ଋ","ଢ଼",
								"ସ","ଶ","ଷ","ଶ୍ର","ତ","ଥ",
								"ଟ","ଠ","ତ୍ର","ୁ","ୂ","ଉ","ଊ",
								"ଵ","ୱ","ବ","ୱ","ଵ","ବ",
								"୍","ୟ","ଯ","ଂ","ଃ","ଁ","଼","ଽ","୰" 
								]
		return button_string_array