class Malayalam(object):
	def __init__(self):
		self.language='Malayalam'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY (BHAML MALAYALAM)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<ഹ്റമാൽ>"
		base_message += "\n\n\t<ഹെഡ്>"
		base_message += "\n\t\t<ടൈറ്റിൽ>भारत कोड</ടൈറ്റിൽ>"
		base_message += "\n\t<സ്കിര്പട് language=""Javascript"">"
		base_message += "\n\n\t\tfunction message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\talert('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</സ്കിര്പട്>"
		base_message += "\n\t</ഹെഡ്>"
		base_message += "\n\n\t<ബോഡി>"
		base_message += "\n\t\t<പി>Hello there! mera naam Nikhil hai!</പി>"
		base_message += "\n\t\t<അ href=""http://www.google.com"">Google</അ>"
		base_message += "\n\t\t<ഇന്പുട് type=button value='कलिक' onClick='message();'></ഇന്പുട്>"
		base_message += "\n\t</ബോഡി>"
		base_message += "\n\n</ഹ്റമാൽ>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"ക"," ഖ","ഗ","ഘ","ങ","ച",
								"ഛ","ജ","ഝ","ഞ","ട","ഠ",
								"ഡ","ഢ","ണ","ത","ഥ","ദ",
								"ധ","ന","പ","ഫ","ബ","ഭ",
								"മ","യ","ര","ല","ള","വ",
								"ഹ","ശ","ഷ","സ","റ","ഴ",
								"ൺ","ൻ","ർ","ൽ","ൾ","ൾ",
								"ൿ","അ","ആ","ഇ","ഈ","ഉ",
								"ഊ","ാ","ി","ീ","ു","ൂ",
								"ഋ","ൠ","ഌ","ൡ","എ","ഏ",
								"ഐ","ഒ","ഓ","ഔ","ൃ","ൄ",
								"ൢ","ൣ","െ","േ","ൈ","ൊ",
								"ോ","ൌ","ം","ഃ","ഽ","൦","൧",
								"൨","൩","൪","൫","൬","൭",
								"൮","൯","൰","൱","൲" 
								]
		return button_string_array