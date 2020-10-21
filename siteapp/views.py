from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import CommentForm, ContactForm
from .models import Post, Comment

def home(request):
    """ Home page of blog this veiw show the 3 last post """
    
    post_list = Post.objects.order_by("-created_at")
    page = request.GET.get("page", 1)
    
    paginator = Paginator(post_list, 3)
    try: 
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
        
    context = {
        'posts': posts
    }
    return render(request, "siteapp/home.html", context)


class PostDetail(FormMixin, DetailView):
    """ Show post detail with generic view 
    """
    template_name = "siteapp/post_detail.html"
    model = Post
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse("site:post_detail", 
                       kwargs={
                           "slug":self.object.slug ,
                           "pk":self.object.id
                        }
                    )
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        #commentForm in context
        context["form"] = CommentForm(initial={'post':self.object})
        context["comments"] = Comment.objects.filter(post_commented=self.object.id)
        
        return context
    
    
    def post(self, request, *args, **kwargs):
        #when user submit a comment
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        new_comment.post_commented_id = self.object.id
        new_comment.save()
        
        return super(PostDetail, self).form_valid(form)
    

class SignUpView(CreateView):
    """Class of creation user """
    template_name = "siteapp/registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("site:home")
    
    
    def form_valid(self, form):
        valid =super().form_valid(form)
        login(self.request, self.object)
        return valid
    


def contact(request):
    """ Contact view who show contact page """
    form = ContactForm()
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            form.save()
            return JsonResponse({"name":name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=200)
    return render(request, 'siteapp/contact.html', {"form":form})
