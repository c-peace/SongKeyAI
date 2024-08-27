from django.shortcuts import render
from SongKeyApp.engine import songKeyAi
from SongKeyApp.models import Data

def analyze(request):
    data = Data()
    result = ["분석값이 나오기까지 약 20초가 소요됩니다. 로딩 중이니 화면이 멈춘 것 같아도 기다려주세요.",""]
    if request.method == 'POST' and data.url != request.POST['url'].split('&')[0]:
        try:
            data.url = request.POST['url'].split('&')[0]

            key, scale, key_strength, tempo, title = songKeyAi.analyzeSong(data.url)

            result = [f"Title : {title}", f'''곡의 키는 : {key} {scale} 이며, 정확도는 {key_strength}% 입니다.
            곡의 빠르기는 : {tempo} 입니다.
            ''']
            data.url = ''
        except:
            return render(request, 'index.html', {'result': "url이 잘못되었습니다. 새로운 url을 입력해주세요."})
        
    return render(request, 'index.html', {'title': result[0], 'result': result[1]})


# 하나의 아이디어!
# render를 사용하지 말고 https로 html을 넘기면 어떨까?
# 계속해서 html 파일을 렌더링하는 것 보다 필요한 부분만 html코드를 계속해서 집어 넣어주면 괜찮지 않을까?
# 하지만 Post가 새로고침할 때 계속해서 나타난다는 문제는 해결해야 한다.

# 두번째 아이디어!
# redirect로 html파일에 접근하는 것!

# 할일
# redirect와 get으로 새로고침 문제를 해결하는데
# 먼저 디자인을 하고 개발을 진행하자!
# 오늘은 여기까지.. ㅋㅋ