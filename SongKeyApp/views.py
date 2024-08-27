from django.shortcuts import render
from SongKeyApp.engine import songKeyAi
from SongKeyApp.models import Data

def analyze(request):
    result = ["분석값이 나오기까지 약 20초가 소요됩니다. 로딩 중이니 화면이 멈춘 것 같아도 기다려주세요.",""]
    if request.method == 'POST':
        try:
            data = Data()
            data.url = request.POST['url']
            data.url = data.url.split('&')[0]

            key, scale, key_strength, tempo, title = songKeyAi.analyzeSong(data.url)

            result = [f"Title : {title}", f'''곡의 키는 : {key} {scale} 이며, 정확도는 {key_strength}% 입니다.
            곡의 빠르기는 : {tempo} 입니다.
            ''']
        except:
            return render(request, 'index.html', {'result': "url이 잘못되었습니다. 새로운 url을 입력해주세요."})
        
    return render(request, 'index.html', {'title': result[0], 'result': result[1]})
