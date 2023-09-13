from django.contrib import messages
from django.http import request

from django.shortcuts import render, redirect
from .models import Post,Tag
from .forms import UserProfileForm

# Create your views here.
#def postlogin(request):
   # return redirect('postlogin.html')
def postlogin(request):
    return render(request,'postlogin.html')



def create_post(request):
    post1 = Post.objects.all()
    if request.method == 'POST':
        # Get form data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        tag_names = request.POST.getlist('tags')
        date = request.POST.get('date')
        is_published = 'is_published' in request.POST  # Check if the 'is_published' checkbox is selected

        # Create a new Post object
        post = Post(
            user=request.user,  # Assign the current user to the post
            title=title,
            description=description,
            publication_date=date,
            is_published=is_published
        )
        post.save()

        # Add tags to the post
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return redirect('post:create_post')  # Redirect to a success page or post list

    return render(request, 'postlogin.html',{'post1':post1})
'''
def create_post(request):
    #post1 = Post.objects.all()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Post Confirmed")

    else:
        form = UserProfileForm()

    return render(request, 'postlogin.html', {'form': form})
'''