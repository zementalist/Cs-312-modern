import json
from operator import contains
from .models import Post
from datetime import datetime
from django.db.models import Q
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


# REQUIRED
def find_by_user(request):
    # Find posts of 'username' John Doe
    # AND likes are greater than 5

    # CODE HERE
    posts = Post.objects.filter(username='John Doe',likes__gt=5)
    # END
    
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

# REQUIRED
def find_by_title(request):
    # Find posts where:
    # Title contains Home
    # AND
    # likes are less than or equal to 6

    # CODE HERE
    posts = Post.objects.filter(title__contains="Home",likes__lt=6)
    # END

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

# REQUIRED
def search_user(request, username):
    # Find posts for a specific user (given)

    # CODE HERE
    posts = Post.objects.filter(username=username)
    # END

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

# REQUIRED
def find_by(request, username, likes):
    # Find posts for a specific user (given)
    # and likes >= any given likes count

    # CODE HERE
    posts = Post.objects.filter(username=username,likes__gte=5)
    # END

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def index(request):
    # Function to return all posts
    
    # START CODE HERE
    # 1- Retrieve all posts
    posts = Post.objects.all()

    # END CODE

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def show(request, id):
    # Function to show a single post
    
    # START CODE HERE

    # 1- Get post by id
    post = Post.objects.get(id=id)
    post.tags = post.body.split()

    # 2- Create the context
    context = {
        'post': post
    }
    # 3- return template 'posts/show.html' with context
    return render(request, 'posts/show.html', context)
    # END CODE



def create(request):
    # Functionn to show post_creation_form template
    return render(request, 'posts/create.html')



def store(request):
    # Function to store new post
    if request.method == "POST":
        # Recieve form data & Create new post
        title, body, image, username, likes = request.POST['title'], request.POST['body'], request.POST['image'], request.POST['username'], request.POST['likes']
        
        if "kids_allowed" in dict.keys(request.POST):
            kids_allowed = True
        else:
            kids_allowed = False
        # STAR CODE HERE
        # 1- Create new post, given the previous variables
        # post = Post.objects.create(title=title,body=body)
        post = Post(title=title,body=body,image=image,username=username, likes=likes, kids_allowed=kids_allowed)
        post.save()
        # 2- Create context with the created post
        context = {
            'post':post
        }
        # 3- return template 'posts/show.html' with context
        return render(request, 'posts/show.html', context)
        # END CODE

    else:
        # request method is not POST
        return redirect('/posts')



def edit(request, id):
    # Function to show post_editing_form template
    if request.method == "GET":

        # START CODE HERE

        # 1- Get post by id
        post = Post.objects.get(id=id)

        # END CODE

        # if post exists
        if post is not None:
            context = {
                'post' : post
            }
            return render(request, 'posts/edit.html', context)
        else:
            # Post is not found
            return render(request, 'posts/not_found.html')
    else:
        # request method is not GET
        return redirect('/dashboard')



def update(request, id):
    # Function to update a row of existing post
    if request.method == "POST":
        # check that request method is PUT
        _method = request.POST['_method'].upper()
        if _method == "PUT":

            # START CODE HERE PART 1
            # 1- Get post by id
            post = Post.objects.get(id=id)
            # END CODE PART 1

            # check that post exists
            if post is not None:
                # Recieve new data & Update post
                title, body, image = request.POST['title'], request.POST['body'], request.POST['image']
                

                # START CODE HERE PART 2
                # 1- Update post values
                post.title = title
                post.body = body
                post.image = image
                # 2- Apply the update to the database
                post.save()
                # END CODE PART 2

                context = {
                    'post' : post,
                    'alert' : {
                        'type' : 'success',
                        'message' : 'Your post is updated successfully.'
                    }
                }
                return render(request, 'posts/show.html', context)
            else:
                # Post is not found
                return render(request, 'posts/not_found.html')
        else:
            # request method is not PUT
            return redirect('/posts')
    else:
        # request method is not POST
        return redirect('/posts')


#REQUIRED
def destroy(request, id):
    # Function to delete existing post
    if request.method == 'POST':
        _method = request.POST['_method'].upper()
        if _method == "DELETE":
            # Init context & retrieve post
            context = {}

            # START CODE HERE PART 1

            # 1- Find post by id
            post = Post.objects.get(id=id)

            # END CODE PART 1

            # if post exists -> delete it
            if post is not None:

                # START CODE HERE PART 2
                
                # 1- Delete post
                post.delete()
                
                # END CODE PART 2

                # Return success message
                context = {
                    'alert': {
                        'type' : 'success',
                        'message' : 'Your post is removed successfully'
                    }
                }
            else:
                # Post is not found, return fail message
                context ={
                    'alert': {
                        'type' : 'danger',
                        'message' : 'Something went wrong, please try again.'
                    }
                }
            # assign alert to session, to redirect with context
            request.session['alert'] = context['alert']
            return redirect('/posts')
        else:
            # request method is not DELETE
            return redirect('/posts')
    else:
        # request method is not POST
        return redirect('/posts')


                        
