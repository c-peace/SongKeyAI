# youtube-dl를 이용해서 url에서 음원을 추출하고 정보들을 수집하는 파일

import yt_dlp as youtube_dl
import essentia.standard as es
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'downloaded_audio.%(ext)s',
}

url = 'https://youtu.be/sgS9ftxn2QQ?si=_V6D2Y3dGfmKJowO'

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

def detect_key(file_path):
    # Load the audio file
    loader = es.MonoLoader(filename = file_path)
    audio = loader()

    # Compute the key of the audio
    key_extractor = es.KeyExtractor()
    key, scale, key_strength = key_extractor(audio)

    return key, scale, key_strength

def detect_tempo(file_path):
    # Load the audio file
    loader = es.MonoLoader(filename = file_path)
    audio = loader()

    # Compute the tempo of the audio
    rhythm_extractor = es.RhythmExtractor()
    tempo = rhythm_extractor(audio)

    return tempo[0]

file_path = 'downloaded_audio.mp3'

key, scale, key_strength = detect_key(file_path)
tempo = detect_tempo(file_path)

print(f'곡의 키는 : {key} {scale} 이며, 정확도는 {int(key_strength * 100)}% 입니다.')
print(f'곡의 빠르기는 : {int(tempo)} 입니다.')

os.remove(file_path)