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
		base_message += "\n\t<ಸ್ಕ್ರಿಪ್ಟ್ language=""Javascript"">"
		base_message += "\n\n\t\tfunction message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\talert('ಭಾಷೆ भारत!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</ಸ್ಕ್ರಿಪ್ಟ್>"
		base_message += "\n\t</ಹೆಡ್>"
		base_message += "\n\n\t<ಬಾಡಿ>"
		base_message += "\n\t\t<ಪ್ಯಾರಾ>Hello there! mera naam Nikhil hai!</ಪ್ಯಾರಾ>"
		base_message += "\n\t\t<ಎ href=""http://www.google.com"">Google</ಎ>"
		base_message += "\n\t\t<ಇನ್ಪುಟ್ type=button value='click me' onClick='message();'></ಇನ್ಪುಟ್>"
		base_message += "\n\t</ಬಾಡಿ>"
		base_message += "\n\n</ಬಿಎಂಎಲ್>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"ಕ","ಖ","ಗ","ಘ","ಙ","ଚ",
								"ಚ","ಛ","ಜ","ಝ","ಞ","ಟ",
								"ಠ","ಡ","ಝ","ಣ","ತ","ಥ",
								"ದ","ಧ","ನ","ಪ","ಫ","ಬ",
								"ಭ","ಮ","ಯ","ರ","ಱ","ಲ",
								"ಳ","ವ","ಹ","ಶ","ಷ","ಸ",
								"ೞ","್","ಅ","ಆ","ಇ","ಈ",
								"ಉ","ಊ","ಾ","ಿ","ೀ","ು",
								"ೂ","ಋ","ಌ","ಎ","ಏ","ಐ",
								"ಒ","ಓ","ಔ","ೃ","ೄ","ೆ",
								"ೇ","ೈ","ೇ","ೊ","ೋ","ೌ",
								"ಂ","ಃ","಼","ೕ","ೖ","೦",
								"೦೧","೨","೩","೪","೫","೬",
								"೭","೮","೯"

								]
		return button_string_array