import TextToSpeech as tts

file_path = 'WantToTranslate.txt'

# ファイルを開く
file = open(file_path, 'r', encoding='utf-8')
# ファイルの中身を読み込む
file_content = file.read()
# ファイルを閉じる
file.close()

# file_content にはファイルの中身が文字列として格納されます
print(file_content)


tts.text_to_speech(file_content, lang='en')
