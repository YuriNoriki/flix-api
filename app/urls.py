from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_view(request):
    return JsonResponse({
        'message': 'Hello word',
        'id': '5',
        'genero':'drama'
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
]
