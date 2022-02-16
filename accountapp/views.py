from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):                        #클래스베이스뷰
    model = User
    form_class = UserCreationForm  #검증 작업
    success_url = reverse_lazy('accountapp:hello_world')            #클래스에선 reverse_lazy 사용하여야한다. reverse는 함수형태에서.
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):                        #디테일뷰
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 10
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView,self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')                                           #일반 펑션을 사용하는 데코레이터를 메소드에 사용할수잇게 변환해주는 데코레이터?
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):                        #클래스베이스뷰
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm                          #name을 수정하지못하게 form을 커스터마이징
    success_url = reverse_lazy('accountapp:hello_world')            #클래스에선 reverse_lazy 사용하여야한다. reverse는 함수형태에서.
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):                        #클래스베이스뷰
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
