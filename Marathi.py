class Marathi(object):
	def __init__(self):
		self.language='Marathi'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- CREATED BY <भमल> (BHAML MARATHI)-BHARAT MARKUP LANGUAGE CODE EDITOR v1.0 -->\n"
		base_message += "<!-------------------- BHAML AUTHOR: NIKHIL MALHOTRA--------------------->\n"
		base_message += "<भमल>"
		base_message += "\n\n\t<हेड​>"
		base_message += "\n\t\t<शीर्षक>भारत कोड</शीर्षक>"
		base_message += "\n\t<लिपी भाषा=""Javascript"">"
		base_message += "\n\n\t\tक्रिया message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\tसूचना('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</लिपी>"
		base_message += "\n\t</हेड​>"
		base_message += "\n\n\t<बौडी>"
		base_message += "\n\t\t<परिच्छेद>Hello there! mera naam Nikhil hai!</परिच्छेद>"
		base_message += "\n\t\t<ए लिंक=""http://www.google.com"">Google</ए>"
		base_message += "\n\t\t<इनपुट प्रकार=बटण value='कलिक' onClick='message();'></इनपुट>"
		base_message += "\n\t</बौडी>"
		base_message += "\n\n</भमल>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"क","ख","ग","घ","ङ","च",
								"छ","ज","झ","ञ","ट","ठ",
								"ड","ढ","ण","त","थ","द",
								"ध","न","प","फ","ब","भ",
								"म","क़","ख़","ग़","ज़","ड़",
								"ढ़","फ़","य","र","ल","ळ",
								"व","ह","श","ष","स","ऱ",
								"ऴ","अ","आ","इ","ई","उ",
								"ऊ","ऋ","ॠ","ऌ","ॡ","ए",
								"ऐ","ओ","औ","्","ा","ि",
								"ी","ु","ू","ृ","ॄ","ॢ",
								"ॣ","े","ै","ो","ौ","ँ",
								"ं","ः","़","A"
								]
		return button_string_array