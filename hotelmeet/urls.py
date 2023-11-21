from django.urls import path
from . import views

app_mane='hotelmeet'

urlpatterns = [
  path('',
       views.IndexView.as_view(),
       name='index'),
  
  path('contact/',
       views.ContactView.as_view(),
       name='contact'),
  
  path('mypage/',
       views.MypageView.as_view(),
       name = 'mypage'),
  
  path('project/',
       views.ProjectView.as_view(),
       name='project'
       ),
  
  path('feature/',
       views.FeaturView.as_view(),
       ),
  
  path('post_photo/',
     views.Post_PhotoView.as_view(),
     name='post_hoto'
     ),
]