from django.urls import path
# viewsモジュールをimport
from . import views
# viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引き出来るように名前をつける
app_name = 'accounts'
# URLパターンを登録するための変数
urlpatterns = [
     # サインアップページのビューの呼び出し
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),
    
    # サインアップ完了ページのビューの呼び出し
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),
    
    # ログインページの表示
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    
    # ログアウトを実行
    path('logout/',
         auth_views.LogoutView.as_view,
         name='logout'),
]
