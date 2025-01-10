DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql", # 사용하는 db 엔진으로 변경
        "NAME": "django_db", # 데이터베이스 이름
        "USER": "root", # DB에 설정한 사용자 계정 이름
        "PASSWORD":"123qwe!@#",
        "HOST": "localhost", # IP주소
        "PORT":"3306",
    }
}
# 기존 setting.py에서 복사해오고, 기존 파일에서는 주석처리 
SECRET_KEY = "django-insecure-$zagl(tj6u1jgc)u9gk&dos51e*9yruho)-^beo)2t0wt%_0l9"
