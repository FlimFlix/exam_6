from webapp.models import UserInfo, Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from webapp.forms import PostCreateForm, PostUpdateForm, UserUpdateForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('-date_created')


class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name = 'user_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostUpdateForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if self.request.user == post.author:
            return super(PostUpdateView, self).dispatch(request, *args, **kwargs)
        elif self.request.user.is_anonymous:
            return redirect('accounts:login')
        else:
            return redirect('webapp:post_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    template_name = 'user_update.html'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('webapp:user_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('webapp:post_list')

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if self.request.user == post.author:
            return super(PostDeleteView, self).dispatch(request, *args, **kwargs)
        elif self.request.user.is_anonymous:
            return redirect('accounts:login')
        else:
            return redirect('webapp:post_list')