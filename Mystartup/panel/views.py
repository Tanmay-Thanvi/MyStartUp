from django.shortcuts import render,redirect
from .models import Profile,Connection
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,"home.html")

def dashboard(request):
    if request.user.is_authenticated:
        objs = Profile.objects.exclude(user=request.user)
        return render(request,"panel.html",{'len':objs})
    else:
        # Message : Please Login First 
        return redirect(home)

def Profile_page(request):
    if request.user.is_authenticated:
        if request.GET:
            user = request.GET["query"]
        else:
            user = request.user.username
        if User.objects.filter(username=user):
            profile_user = User.objects.get(username=user)
        else:
            # Message : User Does Not exist 
            return redirect(dashboard)
        show = True
        connected = False
        hide = False
        c = 0
        c1 = 0
        c2 = 0
        profile = Profile.objects.get(user=profile_user)
        Sender_Connections = Connection.objects.filter(Sender=Profile.objects.get(user=request.user))
        Recieved_Connections = Connection.objects.filter(Reciever=Profile.objects.get(user=request.user))
        All_Connections = list()
        for i in Sender_Connections:
            if i.Acceptance == False:
                c1+=1;
            else:
                c2+=1
            All_Connections.append(i)
            if i.Reciever == profile:
                if i.Acceptance:
                    connected = True
                show = False
        for i in Recieved_Connections:
            All_Connections.append(i)
            if i.Acceptance == False:
                c+=1;
            else:
                c2+=1
            if i.Sender == profile:
                if i.Acceptance:
                    connected = True
                else:
                    hide = True
                show = False
        return render(request,"Profile page.html",{'profile':profile,'sc':Sender_Connections,'rc':Recieved_Connections,"show":show,'connected':connected,'hide':hide,'c':c,'ac':All_Connections,'c1':c1,'len':c2})
    else:
        # Message : Please Login First 
        return redirect(home)

def toggle(request):
    profile = Profile.objects.get(user=request.user)
    profile.Working_status = not(profile.Working_status)
    profile.save()

    # add message working status updated 
    return redirect(Profile_page)

def connect(request):
    if request.method == 'POST':
        sender = Profile.objects.get(user= User.objects.get(username = request.POST['sender']))
        reciever = Profile.objects.get(user= User.objects.get(username = request.POST['reciever']))
        connection = Connection(Sender=sender,Reciever=reciever)
        connection.save()
        # Message : You connected successfully 
    return redirect("/panel/profile/?query="+reciever.user.username)

def accept(request):
    if request.method == 'POST':
        sender = Profile.objects.get(user= User.objects.get(username = request.POST['sender']))
        reciever = Profile.objects.get(user= User.objects.get(username = request.POST['reciever']))
        fromwhich = request.POST['from']
        conn = Connection.objects.get(Sender=sender,Reciever=reciever)
        conn.Acceptance = True 
        conn.save()
        # Message : You are now connected to ...
        if fromwhich == "fromprofile":
            return redirect("/panel/profile/?query="+sender.user.username)
    return redirect("/panel/profile/")

def reject(request):
    if request.method == 'POST':
        sender = Profile.objects.get(user= User.objects.get(username = request.POST['sender']))
        reciever = Profile.objects.get(user= User.objects.get(username = request.POST['reciever']))
        fromwhich = request.POST['from']
        conn = Connection.objects.get(Sender=sender,Reciever=reciever)
        conn.delete()
        if fromwhich == "fromprofile":
                return redirect("/panel/profile/?query="+sender.user.username)
    return redirect("/panel/profile/")

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])