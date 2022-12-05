from django.urls import path

from . import views

# urls.py -> views.py
# views.py : Controller
# models.py : Model
# templates : View

app_name = 'pybo'

urlpatterns = [
    #path('', views.index),
    #path('<int:question_id>/',views.detail)
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
]