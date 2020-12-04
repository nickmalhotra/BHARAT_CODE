class Telugu(object):
	def __init__(self):
		self.language='Telugu'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY (BHAML TELUGU)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<బిమల్>"
		base_message += "\n\n\t<హెడ్>"
		base_message += "\n\t\t<శీర్షిక>भारत कोड</శీర్షిక>"
		base_message += "\n\t<స్క్రిప్ట్ భాష=""Javascript"">"
		base_message += "\n\n\t\tపని message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\tజాగ్రత్త('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</స్క్రిప్ట్>"
		base_message += "\n\t</హెడ్>"
		base_message += "\n\n\t<శరీరం>"
		base_message += "\n\t\t<పేరా>Hello there! mera naam Nikhil hai!</పేరా>"
		base_message += "\n\t\t<ఏ లింక్=""http://www.google.com"">Google</ఏ>"
		base_message += "\n\t\t<ఇన్పుట్ రకం=బటన్ value='कलिक' onClick='message();'></ఇన్పుట్>"
		base_message += "\n\t</శరీరం>"
		base_message += "\n\n</బిమల్>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"క"," ఖ","గ","ఘ","ఙ","చ",
								"ఛ","జ","ఝ","ఞ","ట","ఠ",
								"డ","ఢ","ణ","త","థ","ద",
								"ధ","న","ప","ఫ","బ","భ",
								"మ","య","ర","ఱ","ల","ళ",
								"వ","శ","ష","స","హ","్",
								"అ","ఆ","ఇ","ఈ","ఉ","ఊ",
								"ా","ి","ీ","ు"," ూ","ఋ",
								"ౠ","ఌ","ౡ","ఎ","ఏ","ఐ",
								"ఒ","ఓ","ఔ","ృ","ౄ","ె",
								"ే","ై","ొ","ో","ౌ","ఁ",
								"ం","ః","౦","౧","౨","౩",
								"౪","౫","౬","౭","౮","౯"
								]
		return button_string_array