class Maori(object):
	def __init__(self):
		self.language='Maori'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY (BHAML MAORI)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<BHAML>"
		base_message += "\n\n\t<upoko>"
		base_message += "\n\t\t<taitara>BHAML Code</taitara>"
		base_message += "\n\t<hōtuhi language=""Javascript"">"
		base_message += "\n\n\t\tfunction message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\talert('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</hōtuhi>"
		base_message += "\n\t</upoko>"
		base_message += "\n\n\t<tinana>"
		base_message += "\n\t\t<kōwae>Kia ora! Ko Saket toku ingoa</kōwae>"
		base_message += "\n\t\t<a href=""http://www.google.com"">Google</a>"
		base_message += "\n\t\t<tāuru type=button value='paatohia' onClick='message();'></tāuru>"
		base_message += "\n\t</tinana>"
		base_message += "\n\n</BHAML>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								
								"A","E","H","I","K","M",
								"N","O","P","R","T","U",
								"W","NG","Ā","Ē", "Ī","Ō",
								"Ū"
							 ]


		return button_string_array