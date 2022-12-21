from django.shortcuts import get_object_or_404, render, redirect
from .models import Artwork, Comment
from common.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request): # 홈 페이지
    return render(request, 'index.html')

def explore(request): # 탐색 페이지
    artwork_list = Artwork.objects.all().order_by('-create_date')
    context = {'artwork_list': artwork_list}
    return render(request, 'gallery/explore.html', context)

def detail(request, artwork_id): # 작품의 자세한 페이지
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    context = {'artwork': artwork}
    return render(request, 'gallery/work-single.html', context)

def gallery(request, user_id):
    user = User.objects.get(id=user_id) # 갤러리 페이지
    artwork_list = Artwork.objects.filter(author=user_id).order_by('-create_date')
    context = {'artwork_list': artwork_list, 'user': user}
    return render(request, 'gallery/gallery.html', context)

@login_required(login_url='common:login')
def artwork_upload(request): # 예술품 업로드
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_at = timezone.now()
            post.save()
            return redirect('gallery:detail', artwork_id=post.id)
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'gallery/upload_form.html', context)


@login_required(login_url='common:login')
def artwork_modify(request, artwork_id): # 예술품 수정
    post = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('gallery:detail', artwork_id=post.id)
            #HttpResponseRedirect(request.path_info)
    else:
        form = UploadForm(instance=post)
    context = {'form': form}
    return render(request, 'gallery/upload_form.html', context)


@login_required(login_url='common:login')
def artwork_delete(request, artwork_id): # 예술품 삭제
    post = get_object_or_404(Artwork, pk=artwork_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('gallery:detail', artwork_id=post.id)
    post.delete()
    return redirect('gallery:gallery', user_id=request.user.id)


@login_required(login_url='common:login')
def artwork_likes(request, artwork_id): # 예술품 좋아요
    article = get_object_or_404(Artwork, pk=artwork_id)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        article.like_count -= 1
        article.save()
    else:
        article.like_users.add(request.user)
        article.like_count += 1
        article.save()
    return redirect('gallery:detail', artwork_id)


@login_required(login_url='common:login')
def comment_create(request, artwork_id): # 댓글 생성
    question = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.artwork = question
            comment.save()
            return redirect('gallery:detail', artwork_id=question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'gallery/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify(request, comment_id): # 댓글 수정
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('gallery:detail', artwrok_id=comment.artwork.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('gallery:detail', artwork_id=comment.artwork.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'gallery/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete(request, comment_id): # 댓글 삭제
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('gallery:detail', artwork_id=comment.artwork.id)
    else:
        comment.delete()
    return redirect('gallery:detail', artwork_id=comment.artwork.id)