from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Category
from .forms import PostForm, CategoryForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Post.objects.filter(category=category, status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_object(self):
        return get_object_or_404(
            Post,
            slug=self.kwargs['slug'],
            status='published',
            publish_date__year=self.kwargs['year'],
            publish_date__month=self.kwargs['month'],
            publish_date__day=self.kwargs['day']
        )

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, '¡Post creado exitosamente!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, '¡Post actualizado exitosamente!')
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '¡Post eliminado exitosamente!')
        return super().delete(request, *args, **kwargs)

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'blog/category_form.html'  # Esta es la plantilla correcta
    form_class = CategoryForm
    success_url = '/'  # Redirige a la página principal después de crear la categoría


    def form_valid(self, form):
        messages.success(self.request, '¡Categoría creada exitosamente!')
        return super().form_valid(form)
