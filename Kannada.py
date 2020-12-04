class Kannada(object):
	def __init__(self):
		self.language='Kannada'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY (BHAML KANNADA)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<ಬಿಎಂಎಲ್>"
		base_message += "\n\n\t<ಹೆಡ್>"
		base_message += "\n\t\t<ಶೀರ್ಷಿಕೆ>भारत कोड</ಶೀರ್ಷಿಕೆ>"
		base_message += "\n\t<ಸ್ಕ್ರಿಪ್ಟ್ ಭಾಷೆ=""Javascript"">"
		base_message += "\n\n\t\tಕೆಲಸ message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\tಎಚ್ಚರಿಕೆ('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</ಸ್ಕ್ರಿಪ್ಟ್>"
		base_message += "\n\t</ಹೆಡ್>"
		base_message += "\n\n\t<ಬಾಡಿ>"
		base_message += "\n\t\t<ಪ್ಯಾರಾಗ್ರಾಫ್>Hello there! mera naam Nikhil hai!</ಪ್ಯಾರಾಗ್ರಾಫ್>"
		base_message += "\n\t\t<ಎ ಲಿಂಕ್=""http://www.google.com"">Google</ಎ>"
		base_message += "\n\t\t<ಇನ್ಪುಟ್ ಮಾದರಿ=ಬಟನ್ value='कलिक' onClick='message();'></ಇನ್ಪುಟ್>"
		base_message += "\n\t</ಬಾಡಿ>"
		base_message += "\n\n</ಬಿಎಂಎಲ್>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"ଅ"," ଆ","ା","ବ","ଭ","ଚ",
								"ଛ","କ୍ଷ","ଦ","ଧ","ଡ","ଢ",
								"ଦ୍ଧ","ଦ୍ଵ","ଦ୍ଯ","ଦ୍ଦ","ଦ୍ନ","ଦ୍ମ",
								"େ","ୈ","ଏ","ଐ ୖ","ଫ","ଗ",
								"ଘ","ଙ","ହ","ହ୍ମ","ହ୍ଯ","ହ୍ଲ",
								"ହ୍ନ","ହ୍ଵ","ି"," ୀ","ଇ","ଈ",
								"ଜ","ଝ","ଯ","ଞ","ଜ୍ଞ","କ",
								"ଖ","କ୍ତ","ଲ","ଳ"," ୢ","ଌ",
								"ୡ","ମ","ନ","ଣ","ୋ","ୌ",
								"ଓ","ଔ"," ୗ","ପ","ର"," ୍ର",
								" ୃ","ର୍","ଡ଼୍","ଡ଼","ଋ","ଢ଼",
								"ସ","ଶ","ଷ","ଶ୍ର","ତ","ଥ",
								"ଟ","ଠ","ତ୍ର","ୁ","ୂ","ଉ","ଊ",
								"ଵ","ୱ","ବ","ୱ","ଵ","ବ",
								"୍","ୟ","ଯ","ଂ"," ଃ"," ଁ"," ଼","ଽ","୰" 
								]
		return button_string_array