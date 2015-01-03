from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from login.models import Category,Page,UserProfile
from django.contrib.auth.models import User
from login.forms import CategoryForm,UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import hashlib,datetime,random
from django.utils import timezone



"""def index(request):
    return HttpResponse("Hey there all you need to know <br/><a href='about/'>about us</a>")
"""
def index(request):
    #request.session.set_test_cookie()
    category_list = Category.objects.all()
    context_dict = {'categories':category_list}
    return render(request,'login/index.html',context_dict)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
         
        if form.is_valid():
            form.save(commit=True)
            return index(request) 
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request,'login/add_category.html',{'form':form})
        
        

def about(request):
    return render(request,'login/about.html')

#Handling Registeration and 
def register(request):
    if request.session.test_cookie_worked():
        print ">>>Test Cookie Worked!!"
        request.session.delete_test_cookie()
    registered = False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        #print request.POST.name
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt + email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            user = User.objects.get(username = username)

            
            profile = UserProfile(user = user,activation_key=activation_key,key_expires=key_expires)


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/login/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'punitdama@gmail.com',
                [email], fail_silently=False)

            return render_to_response('login/please_confirm.html')

        else:
            print user_form.errors,profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'login/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def register_confirm(request,activation_key):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    
    user_profile = get_object_or_404(UserProfile,activation_key = activation_key)
    if user_profile.key_expires<timezone.now():
        return render_to_response('login/confirm_expired.html')
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('login/confirm.html')


#Handling login
def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        #remember = request.POST.get('rememberme',None)
        #print remember
        user = authenticate(username=username,password = password)
        #print request.session.get_expiry_age()
        #if not remember:
         #   print "code is executed"
          #  request.session.set_expiry(0)
           # print request.session.get_expiry_age()
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponse('Your account is disabled')
        else:
            print "Invalid login details :{0},{1}".format(username,password)
            return HttpResponse("Invalid Login Details entered")
    else:
        return render(request,'login/login.html',{})

#Handling logout
@login_required
def user_logout(request):
    logout(request)
    HttpResponse("You are not logged in.Redirecting to login page...")
    return HttpResponseRedirect('/login/')


#Removing Category
@login_required
def remove_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        if Category.objects.filter(name=category).exists():
            Category.objects.filter(name=category).delete()
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse("<p>Category doesn't exist.Please check category once again</p><a href='/login/remove_cat'>back</a>")
    else:
        category_list = Category.objects.all()
        context_dict = {'categories':category_list}
        return render(request,'login/remove_cat.html',context_dict)