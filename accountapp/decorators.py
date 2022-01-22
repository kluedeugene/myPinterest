from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])  #프라이머리키로 받은값을 가진 유저오브젝트가 user이다.
        if not user == request.user:
            return HttpResponseForbidden()         # 유저가 일치하지않으면 접근금지
        return func(request, *args, **kwargs)
    return decorated
