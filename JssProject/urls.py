from django.contrib import admin
from django.urls import path, include
# urls는 html 파일을 띄워주는 것만 아니라 함수 호출도 함께 해준다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),
]
