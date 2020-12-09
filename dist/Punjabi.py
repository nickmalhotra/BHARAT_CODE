class Punjabi(object):
	def __init__(self):
		self.language='Punjabi'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY (BHAML PUNJABI)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<ਭਮਲ>"
		base_message += "\n\n\t<ਸਿਰ>"
		base_message += "\n\t\t<ਪਹਿਲਾਂ>भारत कोड</ਪਹਿਲਾਂ>"
		base_message += "\n\t<ਸਕ੍ਰਿਪਟ language=""Javascript"">"
		base_message += "\n\n\t\tfunction message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\talert('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</ਸਕ੍ਰਿਪਟ>"
		base_message += "\n\t</ਸਿਰ>"
		base_message += "\n\n\t<ਸਰੀਰ>"
		base_message += "\n\t\t<ਪੈਰਾ>Hello there! mera naam Nikhil hai!</ਪੈਰਾ>"
		base_message += "\n\t\t<ਏ href=""http://www.google.com"">Google</ਏ>"
		base_message += "\n\t\t<ਇੰਪੁੱਟ type=button value='कलिक' onClick='message();'></ਇੰਪੁੱਟ>"
		base_message += "\n\t</ਸਰੀਰ>"
		base_message += "\n\n</ਭਮਲ>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"ਬ","ਹ","ਗ","ਦ","ਜ","ਜ",
								"ਡ","਼","ੌ","ੈ","ਾ","ੀ",
								"ੂ","ੋ","ੇ","੍","ਿ","ੁ",
								"ਪ","ਰ","ਕ","ਤ","ਚ","ਟ",
								"ੰ","ਮ","ਨ","ਵ","ਲ","ਸ",
								"ਯ","ਔ","ਐ","ਆ","ਈ","ਊ",
								"ਭ","ਙ","ਘ","ਧ","ਝ","ਢ",
								"ਞ","ਓ","ਏ","ਅ","ਇ","ਉ",
								"ਫ","ਖ","ਥ","ਛ","ਠ","ਂ",
								"ਣ","ੲ","ਲ਼","ਸ਼","।","ਗ਼",
								"ਜ਼","ੜ","ਫ਼","ਖ਼",""
								]
		return button_string_array