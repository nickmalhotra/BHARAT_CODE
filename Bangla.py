class Bangla(object):
	def __init__(self):
		self.language='Bangla'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY <ଭମଳ> (BHAML BANGLA)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
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
								"ক","খ","গ","ঘ","ঙ","চ",
								"ছ","জ","ঝ","ঞ","ট","ঠ",
								"ড","ঢ","ণ","ত","থ","দ",
								"ধ","ন","প","ফ","ব","ভ",
								"ম","য়","ড়","ঢ়","য","র",
								"ল","হ","শ","ষ","স","্",
								"অ","আ","ই","ঈ","উ","ঊ",
								"া","ি","ী","ু","ূ","ঋ",
								"ৠ","ঌ","ৡ","এ","ঐ","ও",
								"ঔ","ৃ","ৄ","ৢ","ৣ","ে",
								"ৈ","ো","ৌ","ৎ","ৗ","ঁ",
								"ং","ঃ","়","ঽ","০","১",
								"২","৩","৪","৫","৬","৭","৮",
								"৯" 
								]
		return button_string_array