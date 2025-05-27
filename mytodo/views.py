from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# import bleach




#--------------------------------login page-------------------------------------------------------------
def loginpage(request):
    if(request.method=='POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.info(request, 'Email and password are required')
            return redirect('login')
        
        if  not User.objects.filter(email=email).exists():
            messages.info(request, 'Email not registered')
            return redirect('login')
        
        user=authenticate(request,username=email,password=password)
       

        if user is None:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        
        #if user is not None :
        login(request,user)
        # client_obj = client.objects.get(user=request.user)
        # params = {
        # 'user': request.user,2
        # 'client_obj': client_obj,
        # }
        return redirect('homepage')

            #return render(request,'mytodo/home.html')
    elif request.user.is_authenticated:
        return render(request,'mytodo/home.html')

    else:       
        return render(request,'mytodo/login.html')
#--------------------------------register page-------------------------------------------------------------


def registerpage(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        email = email.lower()

        user = User.objects.filter(email=email)
        if user.exists():
            messages.info(request, 'Email already registered')
            return render(request,'mytodo/register.html')
        
        user = User.objects.create_user(
            first_name=name,
            username=email,
            email=email,
            password=password
        )

        custom_uid = f"UID{str(user.id).zfill(3)}"

        client.objects.create(
            user=user,
            clientid=custom_uid,
            name=name,
            email=email,
            password=password
        )
    return render(request,'mytodo/register.html')



#-------------------------------home page------------------------------------------------------

@login_required(login_url='login')
def homepage(request):

    if not request.user.is_authenticated:
        return redirect('login')

    client_obj = client.objects.get(user=request.user)

    if request.method == 'POST':
        content = request.POST.get('htmlContent')
        if not content:
            messages.warning(request, '⚠️ Content is required')
            return redirect('homepage')
        # allowed_tags = bleach.sanitizer.ALLOWED_TAGS + ['p', 'div', 'br', 'span', 'ul', 'li', 'strong', 'em', 'blockquote','h1']
        # clean_content = bleach.clean(content, tags=allowed_tags)
        # post.objects.create(client=client_obj, content=clean_content)
        post.objects.create(client=client_obj, content=content)
        messages.success(request, 'Post created successfully')
        return redirect('homepage')

    posts = post.objects.filter(client=client_obj).order_by('created_at')
    if not posts.exists():
        messages.info(request, 'ℹ️ No posts available')

    return render(request, 'mytodo/home.html', {
        'user': request.user,
        'client_obj': client_obj,
        'posts': posts,
    })
    


#-----------------------------logout-----------------------------------------------------------------
def logoutpage(request):
    logout(request)
    return redirect('login')
   
    