from recoding import*
import pyaudio
import wave
import datetime

CHUNK = 1024
filename = f"{datetime.date.today()}.wav"

wf = wave.open(filename, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

""" 
   format  : ストリームを読み書きするときのデータ型
   channels: ステレオかモノラルかの選択 1でモノラル 2でステレオ
   rate    : サンプル周波数
   output  : 出力モード

"""

# 1024個読み取り
data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)          # ストリームへの書き込み(バイナリ)
    data = wf.readframes(CHUNK) # ファイルから1024個*2個の

stream.stop_stream()
stream.close()

p.terminate()