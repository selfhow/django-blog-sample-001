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
mkdir D:\_my\git\selfhow\django-blog-sample-001\src  
cd D:\_my\git\selfhow\django-blog-sample-001\src  
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
cd D:\_my\git\selfhow\django-blog-sample-001\src  
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