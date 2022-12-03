from cmath import polar
from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import context
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.views import View
from .models import Posts, Author,Tag
from .forms import Comment, CommentForm
# Create your views here.
all_posts=Posts.objects.all()

class starting_page(ListView):
  template_name="blog/index.html"
  model=Posts
  fields="__all__"
  context_object_name="posts"
  ordering=["-date"]

  def get_queryset(self):
      query=super().get_queryset()
      context=query[:3]
      return context

    
class posts(ListView):
  template_name="blog/all-posts.html"
  model=Posts
  fields="__all__"
  context_object_name="all_posts"
  ordering=["-date"]
  

class post_detail(View):
   def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later
   context_object_name="post"
   def get(self,request,slug):
     post=Posts.objects.get(slug=slug)
     context={
       "post":post,
       "post_tags":post.caption.all(),
       "comment_form":CommentForm(),
       "comments": post.comments.all().order_by("-id"),
       "saved_for_later": self.is_stored_post(request, post.id)
     }
     return render(request,"blog/post-detail.html",context)
     
   def post(self,request,slug):
     comment_form=CommentForm(request.POST)
     post=Posts.objects.get(slug=slug)

     if comment_form.is_valid():
       comment=comment_form.save(commit=False) # It will not hit the database
       comment.post=post
       comment.save()
       return HttpResponseRedirect(reverse("post-detail-page", args=[slug] ))

     context={
       "post":post,
       "post_tags":post.caption.all(),
       "comment_form":comment_form,
       "comments": post.comments.all().order_by("-id"),
       "saved_for_later": self.is_stored_post(request, post.id)
     }
     return render(request,"blog/post-detail.html",context)



class ReadLaterView(View):

  def get(self, request):
        stored_posts = request.session.get("stored_posts") # we use get so that it dosnt crash is session is empty

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Posts.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


  def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)
          
        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")
    
      




