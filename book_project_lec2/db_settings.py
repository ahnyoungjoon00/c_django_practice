SECRET_KEY = "django-insecure-(a@$xdr8lrv#!^(lqp&b0sg%i^3@vq29g!bo_al##m^j64nyn@"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sqldb1", # 데이터베이스 이름
        "USER": "root", # DB에 설정한 사용자 계정 이름
        "PASSWORD":"123qwe!@#",
        "HOST": "localhost", # IP주소
        "PORT":"3306",
    }
}