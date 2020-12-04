class Tamil(object):
	def __init__(self):
		self.language='Tamil'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY <ଭମଳ> (BHAML TAMIL)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<ଭମଳ>"
		base_message += "\n\n\t<ମୁଣ୍ଡ>"
		base_message += "\n\t\t<ଆଖ୍ୟା>भारत कोड</ଆଖ୍ୟା>"
		base_message += "\n\t<ଲିପି ଭାଷା=""Javascript"">"
		base_message += "\n\n\t\tକାର୍ଯ୍ୟ message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\tସତର୍କ('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</ଲିପି>"
		base_message += "\n\t</ମୁଣ୍ଡ>"
		base_message += "\n\n\t<ଶରୀର>"
		base_message += "\n\t\t<ଅନୁଚ୍ଛେଦ>Hello there! mera naam Nikhil hai!</ଅନୁଚ୍ଛେଦ>"
		base_message += "\n\t\t<ଏ ସନ୍ଦର୍ଭ=""http://www.google.com"">Google</ଏ>"
		base_message += "\n\t\t<ଇନପୁଟ୍ ପ୍ରକାର=ବଟନ୍ value='कलिक' onClick='message();'></ଇନପୁଟ୍>"
		base_message += "\n\t</ଶରୀର>"
		base_message += "\n\n</ଭମଳ>"

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