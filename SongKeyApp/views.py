from django.shortcuts import render, HttpResponse
from SongKeyApp.engine import songKeyAi
from SongKeyApp.models import Data


def index(request):
    return render(request, 'index.html', {'result': "분석값이 나오기까지 약 20초가 소요됩니다. 화면이 멈춘 것 같아도 기다려주세요."})


def analyze(request):
    result = ''
    if request.method == 'POST':
        data = Data()
        data.url = request.POST['url']
        data.save()

        key, scale, key_strength, tempo = songKeyAi.analyzeSong(data.url)

        result = f'''곡의 키는 : {key} {scale} 이며, 정확도는 {key_strength}% 입니다.
        곡의 빠르기는 : {tempo} 입니다.
        '''

    return render(request, 'index.html', {'result': result})
