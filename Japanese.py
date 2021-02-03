class Japanese(object):
	def __init__(self):
		self.language='Japanese'


	def base_file_message(self):
		base_message = ""
		base_message += "<!-- 作成者 (BHAML Japanese)-バーラットマークアップ言語エディター v1.0 -->\n"
		base_message += "<!-------------------- バハムルの著者 ヴァイブ・ティワリ--------------------->\n"
		base_message += "<バマル>"
		base_message += "\n\n\t<ヘッド>"
		base_message += "\n\t\t<スクリプツ >スクリプツ</スクリプツ>"
		base_message += "\n\t<スクリプツ language=""Javascript"">"
		base_message += "\n\n\t\tfunction message()"
		base_message += "\n\n\t\t{"
		base_message += "\n\n\t\t\talert('hello world!');"
		base_message += "\n\n\t\t}"
		base_message += "\n\n\t</スクリプツ>"
		base_message += "\n\t</ヘッド>"
		base_message += "\n\n\t<ボディー>"
		base_message += "\n\t\t<パラー>Hello there! mera naam Vaibhav hai!</パラー>"
		base_message += "\n\t\t<アー href=""http://www.google.com"">Google</アー>"
		base_message += "\n\t\t<インプット type=button value='クリック' onClick='message();'></インプット>"
		base_message += "\n\t</ボディー>"
		base_message += "\n\n</バマル>"

		return base_message 

	def button_strings(self):
		button_string_array = [
								"ア", "イ", "ウ", "エ", "オ", 
								"カ", "キ", "ク", "ケ", "コ", 
								"サ", "シ", "ス", "セ", "ソ", 
								"タ", "チ", "ツ", "テ", "ト", 
								"ナ", "ニ", "ヌ", "ネ", "ノ", 
								"ハ", "ヒ", "フ", "ヘ", "ホ", 
								"マ", "ミ", "ム", "メ", "モ", 
								"ヤ",      "ユ",      "ヨ", 
								"ラ", "リ", "ル", "レ", "ロ", 
								"ワ", "ヰ",      "ヱ", "ヲ", 
								                    "ン",
								"ガ", "ギ", "グ", "ゲ", "ゴ", 
								"ザ", "ジ", "ズ", "ゼ", "ゾ", 
								"ダ", "ヂ", "ヅ", "デ", "ド", 
								"バ", "ビ", "ブ", "ベ", "ボ", 
								"パ", "ピ", "プ", "ペ", "ポ", 

								"ァ", "ィ", "ゥ", "ェ", "ォ", 
								"ー"
							 ]


		return button_string_array
