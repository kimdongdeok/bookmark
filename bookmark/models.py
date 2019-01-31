from django.db import models

# Create your models here.
# 모델을 작성
# 모델 : 데이터베이스의 묘사 - 어떤 테이블을 만들것이진 어떤컬럼을 만들것인지 어떤 제약조건을 둘것인지

# models.Model
# 장고에서 모델은 ORM이란 기능을 통해서 프로그래머가 SQL을 몰라도 데이터베이스를 사용할 수 있도록 도와줍니다.
# models.Model이 실질적인 기능 함수를 가지고 있다.

# 모델까지 만들었을 경우 : 아직DB에 반영이 안된 상태
# makemigrations, migrate

# python manage.py makemigrations bookmark

# python manage.py sqlmigrate bookmark 0001

# python manage.py migrate bookmark 0001

# 데이터베이스에 직접 접근하는 방법: python manage.py dbshell
# 데이터베이스에 간접 접근하는 방법: python manage.py

class Bookmark(models.Model):

   # 클래스 변수, 속성 : 데이터베이스 컬럼
   # 문자열, 숫자, Boolean, binary
   # 각 필드의 제약 조건: 컬럼의 제약조건
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

   # 필드 종류 : 프로트 페이지에서 어떤 폼 태그를 사용할 것인지, 폼태그에서 제약조건

    def __str__(self):
        # 객체를 출력할때 나타날 값
        return self.site_name + " : " + self.url

    #모델 내부의 메서드들은 필드처럼 사용될 수 있다.
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail, args=[str(self')

    # 다양한 정보를 갖는 클래스
    class Meta:
        ordering = ['site_name']