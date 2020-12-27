from django.shortcuts import render
from lodin.models import Newuser
from django.contrib import messages

def Indexpage(request):
	return render(request,'index.html')

def Userreg(request):
	if request.method=='POST':
		Username=request.POST['username']
		Email=request.POST['email']
		Password=request.POST['password']
		Age=request.POST['age']
		Gender=request.POST['gender']
		MartialStatus=request.POST['martialStatus']
		Newuser(Username=Username,Email=Email,Password=Password,Age=Age,Gender=Gender,MartialStatus=MartialStatus).save()
		messages.success(request,"The new user"+ request.POST['username'] +"Is saved successfully")
		return render(request,'Registration.html')
	else:
		return render(request,'Registration.html')

def loginpage(request):
	if request.method=='POST':
		try:
			Userdetails=Newuser.objects.get(Email=request.POST['email'],Password=request.POST['password'])
			print("Username=",Userdetails)
			request.session['Email']=Userdetails.Email
			return render(request,'index.html')
		except Newuser.DoesNotExist as e:
			messages.success(request,'username /password Invalid...!')
	return render(request,'Login.html')


def logout(request):
	try:
		del request.session['Email']
	except:
		return render(request,'index.html')
	return render(request,'index.html')
				





		
	