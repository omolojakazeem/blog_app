from django.urls import path
from . import views as v


app_name = 'blog'

urlpatterns = [
    path('', v.post_list, name='post_list'),
    path('<int:id>/', v.post_detail, name='post_detail')
]
