from gtts import gTTS
import subprocess
import os

def text_to_speech(text, lang='en'):
    # gTTSオブジェクトを作成
    tts = gTTS(text=text, lang=lang, slow=False)
    
    # 音声ファイルを保存
    tts.save("output.mp3")
    
    # OS標準の音声プレーヤーで再生
    subprocess.run(["afplay", "output.mp3"])
    
    # 再生が完了したらファイルを削除
    os.remove("output.mp3")