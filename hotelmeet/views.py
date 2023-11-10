from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
  # index.htmlをレンダリングする
  template_name = 'index.html'
  # object_listキーの別名を設定
  context_object_name = 'orderby_records'
  # 1ページに表示するレコード件数を設定
  paginate_by = 4

class LoginView(TemplateView):
  template_name = 'login.html'

class ContactView(TemplateView):
  template_name = 'contact.html'