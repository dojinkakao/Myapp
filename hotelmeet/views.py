from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import RoomPost
from .models import RoomPost
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse_lazy

class IndexView(TemplateView):
  # index.htmlをレンダリングする
  template_name = 'index.html'
  # object_listキーの別名を設定
  context_object_name = 'orderby_records'
  # 1ページに表示するレコード件数を設定
  paginate_by = 4

class ContactView(TemplateView):
  template_name = 'contact.html'
  
class UserView(ListView):
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      # self.kwargsでキーワードの辞書を取得し、
      # userキーの値(ユーザーテーブルのid)を取得
      user_id = self.kwargs['user']
      # filter(フィールド名=id)で絞り込む
      user_list = PhotoPost.objects.filter(
        user=user_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return user_list


class MypageView(ListView):
    # mypage.htmlをレンダリングする
    template_name ='mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      queryset = RoomPost.objects.filter(
        user=self.request.user).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return queryset
      
  #ここから
class ProjectView(TemplateView):
  template_name='project.html'
 
class FeaturView(TemplateView):
  template_name='feature.html'
 
class Post_PhotoView(TemplateView):
  template_name='post_photo.html'
  #ここまで(太田)

class ContactView(FormView):
  
  template_name = 'contact.html'
  
  form_class = ContactForm
  
  success_url = reverse_lazy('blogapp:contact')
  
  def form_valid(self, form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    title = form.cleaned_data['title']
    message = form.cleaned_data['message']
    
    subject = 'お問い合わせ: {}'.format(title)

    message = \
      '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
        .format(name, email, title, message)
    #　メールの送信元アドレス
    from_email = 'mcd2376099@stu.o-hara.ac.jp'
    #　送信先のメールアドレス
    to_list = ['mcd2376099@stu.o-hara.ac.jp']
    
    message = EmailMessage(subject=subject,
                           body=message,
                           from_email=from_email,
                           to=to_list,
                           )
    message.send()
    messages.success(
        self.request, 'お問い合わせは正常に送信されました。')
    
    return super().form_valid(form)