from django.shortcuts import render
from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    #template_name = 'aaa.html' # 내가 원하는 파일로 직접 지정
    template_name_suffix = '_create' # bookmark_create.html

    model = Bookmark
    
    #입력받을 필드 목록
    fields = ['site_name','url']
    
    #완료된후 이동할 페이지
    # reverse
    # url 패턴 -> url
    # lazy
    # lazy가 없으면 바로 url이 만들어져 있는형태
    # lazy가 있으면 실행할 때 url을 만들어서 던져줌.
    success_url = reverse_lazy('bookmark:index') # url 의 namespace를 참조한다.


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')