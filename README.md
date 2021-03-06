# 프로젝트의 목적  
python django (파이썬 장고) 2.0 기초 익히기 위한 프로젝트입니다.  
  
# 참고  
[Django girls](https://tutorial.djangogirls.org/ko/django_installation/)  
  
# 파이썬 다운로드  
[파이썬 다운로드](https://www.python.org/downloads/)  
2018.04.10 현재 파이썬 버전 3.6버전대입니다.  
  
옛날 버전은  
* [windows](https://www.python.org/downloads/windows/)  
* [리눅스](https://www.python.org/downloads/source/)  
* [맥 OS X](https://www.python.org/downloads/mac-osx/)  
* [기타](https://www.python.org/download/other/)  
  
에서 다운로드하면 됩니다.  
참고로 이 프로젝트는 **python 3.5** 버전으로 진행. 3.4 이상 버전이라면 별 차이는 없습니다. (~~무책임~~)  
  
# virtualenv  
virtualenv는 개별 파이썬 환경을 생성하는 것이라고 생각하면 편합니다.  
각 프로젝트마다 파이썬 버전이 다르거나, 사용하는 라이브러리가 다르다면 정신건강에 해롭습니다.  
그럴때를 대비해서 virtualenv 를 이용해서 개별 환경을 따로 세팅합니다.  
  
## windows  
cmd 에서 생성해야 합니다.  
윈도우 8버전 이후로는 Windows + R => cmd 로 들어가면 관리자 권한이 아니어서 제약이 있습니다.  
따라서 ```window 버튼 -> cmd -> 명령 프롬프트 우클릭 -> 관리자 권한으로 실행``` 을 권합니다.  
  
### virtualenv 생성  
```  
mkdir 프로젝트 경로  
cd 프로젝트 경로  
python -m venv 가상환경 이름  
```  
  
#### 샘플  
```  
d:  
mkdir D:\_my\git\selfhow\django-blog-sample-001  
cd D:\_my\git\selfhow\django-blog-sample-001  
python -m venv venv35  
```  
  
다 끝나도 원래 아무 메세지도 안 나오니까 당황할 필요 없습니다.  
  
### 사용  
  
```  
cd 프로젝트 경로  
가상환경이름\scripts\activate  
```  
  
```  
d:  
cd D:\_my\git\selfhow\django-blog-sample-001  
venv35\scripts\activate  
```  
  
커맨드 앞에 (venv35) 이런 식으로 가상환경 이름이 나오면 성공입니다.  
  
## 리눅스  
### 생성  
```  
cd /home  
python3 -m venv venv35  
```  
  
다 끝나도 원래 아무 메세지도 안 나오니까 당황할 필요 없습니다.  
  
### 사용  
```  
cd /home  
. venv35/bin/activate  
```  
  
커맨드 앞에 (venv35) 이런 식으로 가상환경 이름이 나오면 성공입니다.  
  
# django 설치  
virtualenv 실행 후에 아래 커맨드를 입력하세요.  
```  
pip install django  
```  
  
2018.04.10 현재 django 2.0.4 버전이 최신 버전입니다.  
  
pip 는 python 중앙 리파지터리 pypi에서 소스를 받아와서 자동으로 내 컴퓨터에 설치해 주는 명령입니다.  
pip 로 설치가 끝나면 pytz, django 두 개의 라이브러리가 설치되어 있습니다.  
  
## 확인  
### 윈도우  
```  
dir venv35\Lib\site-packages  
```  
  
django 디렉토리와, pytz 디렉토리가 보여야 합니다.  
  
### 리눅스  
```  
ls venv35/lib/site-packages  
```  
django 디렉토리와, pytz 디렉토리가 보여야 합니다.  
  
# 만약 git으로 관리하려면 가상 환경은 빼버립시다.  
굳이 가상 환경을 github에 올릴 필요는 없으니까요.  
  
## .gitignore 파일 생성  
github 루트 디렉토리에 .gitignore 라는 파일을 만듭니다.  
  
그리고 아래 내용을 적습니다.  
```  
venv35  
```  
  
끝입니다.  
이렇게 하면 git에서 venv35 라는 가상 환경은 관리하지 않게 됩니다.  
  
# django 프로젝트 생성  
드디어 프로젝트를 생성합시다.  
그 전에 virtualenv 안에 들어와 있는지 꼭 확인하세요.  
```  
cd 프로젝트  
django-admin.py startproject 프로젝트명 .  
```  
  
마지막에 . 이 있는 것을 빼먹으면 안되요.  
.은 현재 디렉토리 아래에 만들겠다는 뜻입니다.  
  
  
## 샘플예제  
```  
d:  
mkdir D:\_my\git\selfhow\django-blog-sample-001\src  
cd D:\_my\git\selfhow\django-blog-sample-001\src  
django-admin.py startproject selfhowblog .  
```  
  
저는 github으로 프로젝트를 관리하기 위해 소스 폴더를 따로 빼고 src라고 이름 붙였습니다.  
selfhowblog 는 프로젝트 이름입니다.  
이렇게 하면 디렉토리 구조는 이런식으로 됩니다.  
```  
django-blog-sample-001  <= github 루트 디렉토리  
django-blog-sample-001\venv35 <= 가상환경  
django-blog-sample-001\src <= django 프로젝트 루트  
django-blog-sample-001\src\selfhowblog  <= django 프로젝트의 메인 앱.  
```  
  
## 확인해 보기  
장고에 내장된 웹서버로 일단 제대로 설치되었나 확인하는 순간입니다.  
  
```  
cd django_프로젝트_루트_디렉토리  
python manage.py runserver  
```  
  
뭔가 메세지가 어쩌구 나오면 웹브라우저로 가서 [http://localhost:8000](http://localhost:8000) 으로 접속해 봅니다.  
  
**The install worked successfully! Congratulations!**  
이런 메세지가 나오면 잘 설치된 겁니다.  
저도 같이 축하드립니다.  
  
### 샘플예제  
```  
d:  
cd D:\_my\git\selfhow\django-blog-sample-001\src  
python manage.py runserver  
```  
  
  
# 아주 기본적인 설정하고 지나가기  
django 앱의 세팅은 프로젝트 루트의 settings.py에서 시작합니다.  
경로는 ```/django-blog-sample-001/src/selfhowblog/settings.py``` 입니다.  
  
## 타임존  
```  
TIME_ZONE = 'UTC'  
```  
이렇게 되어 있는 부분을  
```  
TIME_ZONE = 'Asia/Seoul'  
```  
이렇게 바꿔줍니다.  
  
이유는? 한국인이니까요. :)  
  
## static url  
웹서버의 정적 url 주소 세팅을 하는 부분입니다.  
정적 url이라 함은 , 서버쪽 코드가 아니라 클라이언트쪽 코드, 즉 css나 자바스크립트 등을 넣어놓는 공간이죠.  
  
파일 가장 아래에 이렇게 써 있습니다.  
```  
STATIC_URL = '/static/'  
```  
  
그 아래에 STATIC_ROOT 를 넣어줍니다.  
```  
STATIC_URL = '/static/'  
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  
```  
  
이제 웹서버에서 /static으로 접근할 수 있게 되었습니다. 만세.  
  
## 데이터베이스  
```  
DATABASES = {  
'default': {  
'ENGINE': 'django.db.backends.sqlite3',  
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  
}  
}  
```  
이렇게 설정이 되어 있는데요.  
기본값은 sqlite입니다.  
  
일단은 그냥 두고 프로젝트를 진행하도록 하지요.  
  
# 데이터베이스 마이그레이션  
마이그레이션은 settings.py 의 ```INSTALLED_APPS``` 항목을 보고 데이터베이스 테이블을 생성해주는 기능입니다.  
```  
  
INSTALLED_APPS = [  
'django.contrib.admin',  
'django.contrib.auth',  
'django.contrib.contenttypes',  
'django.contrib.sessions',  
'django.contrib.messages',  
'django.contrib.staticfiles',  
]  
```  
현재 settings.py 파일은 위와 같이 되어 있습니다.  
  
마이그레이션을 실행해 보겠습니다.  
```  
cd django_프로젝트_루트_디렉토리  
python manage.py migrate  
```  
  
실제로는 아래처럼 되겠죠?  
```  
d:  
cd D:\_my\git\selfhow\django-blog-sample-001\src  
python manage.py migrate  
```  
  
실행시켜 보면 뭔가 계속 아래로 내려가면서 ok가 나올 겁니다.  
  
참고로 개별 모델에만 마이그레이션을 실행하고 싶으면 이렇게 합니다.  
```  
python manage.py migrate 개별모델이름  
```  
  
물론 개별모델은 settings.py 의 INSTALLED_APPS 안에 정의되어 있어야 합니다.  
  
# 앱 생성  
django에서는 개별 기능을 하는 모듈을 앱이라고 부릅니다.  
이제 블로그 앱을 한번 만들어 봅시다.  
  
```  
python manage.py startapp blog  
```  
  
blog가 앱 이름입니다.  
  
이제 /django-blog-sample-001/src/blog 디렉토리가 생긴걸 확인할 수 있습니다.  
  
  
# 앱 등록  
앱을 생성했다고 끝은 아닙니다.  
앱을 등록해야죠.  
django-blog-sample-001\src\settings.py 를 열고 INSTALLED_APPS 안에 blog항목을 추가합니다.  
  
```  
INSTALLED_APPS = [  
'django.contrib.admin',  
'django.contrib.auth',  
'django.contrib.contenttypes',  
'django.contrib.sessions',  
'django.contrib.messages',  
'django.contrib.staticfiles',  
'blog', # 여기가 추가된 부분입니다.  
]  
```  
  
# 모델링  
모델링이라는 건 특정 앱이 어떤 식으로 데이터베이스를 저장할 것인가를 결정하는 일을 말합니다.  
블로그에서 가장 중요한 건 "글" 이죠.  
글은 아마도 몇가지 특성이 있을텐데요.  
예를 들면 **저자**, **제목**, **내용**, **만든날짜**, **발행날짜** 등이겠죠.  
  
## 모델 추가  
모델은 데이터를 나타내는 클래스입니다.  
보통은 데이터베이스 테이블 하나에 모델 클래스를 하나씩 매핑합니다.  
/django-blog-sample-001/src/blog/models.py 파일을 열어보세요.  
  
```  
from django.db import models  
  
# Create your models here.  
```  
  
이렇게 되어있는 부분을 아래처럼 수정하세요.  
  
```  
from django.db import models # 상속을 위해 import  
from django.utils import timezone # created_date의 기본값을 위해 설정.  
  
class Post(models.Model): # 반드시 클래스명은 대문자로 시작할 것. 모델 상속  
author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 저자. django에 기본으로 들어있는 유저의 FK.  
title = models.CharField(max_length=200) #제목. 최대 200글자.  
text = models.TextField() # 내용  
created_date = models.DateTimeField(default=timezone.now) # 생성일. timezone.now() 처럼 현재 시간이 아니라 함수가 넘어가는 것에 주의.  
published_date = models.DateTimeField(blank=True, null=True) # 발행일  
  
def publish(self): # 실제 DB에 저장  
self.published_date = timezone.now()  
self.save()  
  
def __str__(self): # 그냥 print를 찍으면 객체가 보여서 아무런 도움도 안되므로 제목이 보이게 설정.  
return self.title  
```  
  
개별 필드 타입은 [공식 문서](https://docs.djangoproject.com/en/2.0/ref/models/fields/) 를 참고하세요.  
  
## 마이그레이션 파일 준비  
모델 추가 후에는 마이그레이션 파일 준비가 필요합니다.  
마이그레이션 파일은 실제로 django가 마이그레이션을 하기 위해서 준비해 놓은 파일입니다.  
만약 모델클래스가 수정되면 마이그레이션을 추가해야 하고, 이렇게 복잡한 절차를 거침으로써 언제든지 데이터베이스 스키마를 예전 상태로 돌릴 수 있는 장점을 가지게 되죠.  
  
```  
python manage.py makemigrations blog  
```  
  
django-blog-sdample-001/src/blog/migrations/0001_initial.py 가 생기면 성공입니다.  
  
아마도 0001_initial.py 파일의 내용은 아래와 같을 꺼에요.  
```  
# Generated by Django 2.0.4 on 2018-04-11 01:32  
  
from django.conf import settings  
from django.db import migrations, models  
import django.db.models.deletion  
import django.utils.timezone  
  
  
class Migration(migrations.Migration):  
  
initial = True  
  
dependencies = [  
migrations.swappable_dependency(settings.AUTH_USER_MODEL),  
]  
  
operations = [  
migrations.CreateModel(  
name='Post',  
fields=[  
('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  
('title', models.CharField(max_length=200)),  
('text', models.TextField()),  
('created_date', models.DateTimeField(default=django.utils.timezone.now)),  
('published_date', models.DateTimeField(blank=True, null=True)),  
('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),  
],  
),  
]  
  
```  
  
id 열은 자동으로 생성된다는 점에 유의하세요.  
  
## 실제 마이그레이션 실행  
마이그레이션 파일이 생성되었다고 해도 데이터베이스에 반영이 된 건 아닙니다.  
이제 진짜로 데이터베이스 스키마를 변경해 보죠.  
  
```  
python manage.py migrate blog  
```  
  
```Applying blog.0001_initial... OK``` 메세지가 나오면 성공입니다.  
  
# django admin  
이제 django가 자랑하는 admin 입니다.  
  
## 관리자 아이디 생성  
```  
python manage.py createsuperuser  
```  
  
콘솔로 유저이름 / 이메일 / 비밀번호 를 물어봅니다.  
유저이름 : selfhow  
이메일 : 비워둠  
비밀번호 : selfhowcom  
비밀번호 확인 : selfhowcom  
로 일단 해 둡니다.  
원하시는 걸로 해 둬도 별 관계 없습니다.  
다만 비밀번호는 8글자 이상이어야 합니다.  
  
  
## admin에 모델 등록  
이전에 만들었던 Post 모델을 자동으로 관리할 수 있게 해 주죠.  
  
/django-blog-sample-001/src/blog/admin.py  
  
파일을 열어보세요.  
```  
from django.contrib import admin  
  
# Register your models here.  
```  
  
우리가 만든 모델을 admin에서 관리할 수 있게 추가해 줍니다.  
  
```  
from django.contrib import admin  
  
# Register your models here.  
  
from .models import Post # 모델을 불러오고  
admin.site.register(Post) # 모델을 등록.  
```  
  
이렇게 수정하세요.  
  
## 이제 확인할까요?  
일단 서버를 띄우고  
```  
python manage.py runserver  
```  
  
웹브라우저에서 확인합니다.  
[http://localhost:8000/admin](http://localhost:8000/admin)  
  
아까 입력한 아이디와 비밀번호를 입력하세요.  
멋지게 관리자가 나오면 성공입니다.