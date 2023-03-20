from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from panel import views
from panel.models import Profile
# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST['Email']
        password = request.POST['Password']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username, password=password)
            if user is not None:
                auth.login(request, user)
                if Profile.objects.filter(user=request.user).exists():
                    return redirect(views.home)
                else:
                    return redirect(complete_profile)
            else:
                messages.error(request, "Invalid Credentials")
        else:
            messages.error(request, "User does not exist.")
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        name = request.POST['Name']
        fname = name.split(" ")[0]
        lname = name.split(" ")[1]
        email = request.POST['Email']
        password = request.POST['Password']
        if User.objects.filter(email=email).exists():
            messages.error(request, "Account on this mail id already exist!")
        else:
            user = User.objects.create_user(
                username=name, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            messages.success(request, 'Sign-up successful. You can login now')
    return redirect(login)


def logout(request):
    auth.logout(request)
    # Message : Logged out successfully 
    return redirect('/')


def complete_profile(request):
    if request.user.is_authenticated:
        user = request.user
        if (Profile.objects.filter(user=request.user).exists()):
            # Message : Already completed your profile want to edit ? 
            return redirect(views.home)
        
        for i in request.POST:
            print(i,request.POST[i])

        if request.method == "POST":
            pemail = request.POST['pemail']
            mobile = request.POST['mobile']
            gender = request.POST['gender']
            clg_org = request.POST['clg_org']
            branch = request.POST['branch']
            year = request.POST['year']
            if request.POST['status'] == "W":
                status = True
            else:
                status = False
            domain = request.POST['domain']
            linkedin = request.POST['linkedin']

            # if request.FILES != {}:
            pphoto = request.FILES['profilephoto']
            skills = {'Skill No.1 ':request.POST['skill_1'],'Skill No.2 ':request.POST['skill_2'],'Skill No.3 ':request.POST['skill_3']}
            achievements = {'Achievement No.1 ':request.POST['achievement_1'],'Achievement No.2 ':request.POST['achievement_2'],'Achievement No.3 ':request.POST['achievement_3']}
            pobj = Profile.objects.create(user=request.user, Email=pemail, Mobile=mobile, Linkedin=linkedin, Domain=domain,
                                          Year=year, Working_status=status, Clg_Org=clg_org, Gender=gender, Branch_Dept=branch, Profile_photo=pphoto,Skills=skills,Achivements=achievements)
            pobj.save()
            # Message : Profile updated successfully 
            return redirect(views.home)
        return render(request, 'index.html')
    else:
        # Message : Please Login First 
        return redirect(views.home)


def edit_profile(request):
    if request.user.is_authenticated:
        if not(Profile.objects.filter(user=request.user).exists()):
            # Message : Complete your profile first want to complete ? 
            return redirect(views.home)
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            profile.Email = request.POST['pemail']
            profile.Mobile = request.POST['mobile']
            profile.Gender = request.POST['gender']
            profile.Clg_Org = request.POST['clg_org']
            profile.Branch_Dept = request.POST['branch']
            profile.Year = request.POST['year']
            if request.POST['status'] == "W":
                profile.Working_status = True
            else:
                profile.Working_status = False
            profile.Domain = request.POST['domain']
            profile.Linkedin = request.POST['linkedin']

            if request.FILES != {}:
                profile.Profile_photo = request.FILES['profilephoto']
            #message : Profile updated successfully 
            profile.save()
            return redirect(views.Profile_page)
        return render(request, 'editprofile.html', {'profile': profile})
    else:
        # Message : Please Login First 
        return redirect(views.home)
