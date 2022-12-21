from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from common.forms import UserForm
from common.models import User

def signup(request): # 회원가입
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('gallery:gallery', user.id)
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request, exception):
    return render(request, 'common/404.html', {})
