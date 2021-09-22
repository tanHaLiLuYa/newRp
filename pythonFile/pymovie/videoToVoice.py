# from moviepy.editor import *

# video = VideoFileClip('videoplayback.mp4')
# audio = video.audio
# audio.write_audiofile('test.wav')
import speech_recognition as sr
# from pydub import AudioSegment
# import wave
# f = wave.open(r'D:\github\pythonFile\pymovie\test.wav')
# timelength=int(f.getparams()[3]/f.getparams()[2])
# readaudio=AudioSegment.from_wav(r'D:\github\pythonFile\pymovie\test.wav')
# kn=int(timelength/30)+1
# for i in range(kn):#      
#     readaudio[i*30*1000:((i+1)*30+2)*1000].export('D:\\github\\pythonFile\\pymovie\\test{}.wav'.format(i+1), format="wav")




r = sr.Recognizer()


with sr.WavFile('test1.wav') as source:
    audio = r.record(source)
    IBM_USERNAME = "435cc1ce-779b-4c51-8aa6-215aefbc2635"
    IBM_password = "veSOY0er49A9uW6aQpolJ6hcKfoDp1Fa3St1bhnwWfCO"
    text = r.recognize_ibm(audio, username=IBM_USERNAME,
                           password=IBM_password, language="zh-CN")
    print(text)


# https://www.jianshu.com/p/38f148c15327 简书网页

#  import eyed3
#  import wave
#  import os
#  import speech_recognition as sr#
#  from pydub import AudioSegment
#  import timeimport datetime#
# ##获取音频时长#
# f = wave.open(r"C:\Users\Esri\Desktop\speech.wav","rb")
# timelength=int(f.getparams()[3]/f.getparams()[2])
# print(int(5.6))##
#  # 音频分割输出
# readaudio=AudioSegment.from_wav(r'C:\Users\Esri\Desktop\speech.wav')
# kn=int(timelength/30)+1
# for i in range(kn):#      
#     readaudio[i*30*1000:((i+1)*30+2)*1000].export(r'C:\Users\Esri\Desktop\speech\speech%d.wav'%(i+1), format="wav")
#     # 获取文件夹下的音频文件名
#     starttime = datetime.datetime.now()i = 1
#     for name in os.listdir(r'C:\Users\Esri\Desktop\speech'):    
#         print("%d %s 开始转换" % (i, name))   
        
