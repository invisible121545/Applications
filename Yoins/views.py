from django.shortcuts import render
from .models import Products,Admin
from django.views import generic
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import hashlib
# Create your views here.

class indexView(generic.ListView):
	model = Products
	template_name = 'index.html'
	context_object_name = 'products'
	def get_queryset(self):
		return Products.objects.order_by('-products_date_added')[:60]

class loginView(generic.ListView):
	template_name = 'signup.html'
	def get_queryset(self):
		context = {'title':'loginView','is_log':True}
		return context

def product_list(request):
	context = {
		'title':'Buy Cheap Clothes Online, Newchic Clothing Wholesale | newchic.com Mobile',
		'products':Products.objects.all()[:99]
	}
	return render(request,'index.html',context)

def checkSign(request):
	try:
		str = request.POST['admin_pass'].encode('utf-8')
		psw = hashlib.md5(str).hexdigest();
		Admin.objects.get(admin_name=request.POST['username'],admin_pass=psw)
	except (KeyError, Admin.DoesNotExist):
	 	return render(request,'signin.html',{'message':'Wrong Email or password'})
	else:
		return HttpResponseRedirect(reverse('Yoins:product_list'))	
		
def ckeckSignName(request):
	# try:
	user = Admin.objects.get(admin_name=request.POST['username'])
	if user:
		return HttpResponse('Username already exeit!')
	# except e:
	# 	return render(request,'login.html',e.error_message)		


def signup(request):
	# try:
	str = request.POST['admin_pass'].encode('utf-8')
	psw = hashlib.md5(str).hexdigest();
	newuser = Admin(admin_name=request.POST['username'],admin_pass=psw,admin_email=request.POST['email'])
	newuser.save()
	print (newuser)
	return HttpResponseRedirect(reverse('Yoins:product_list'))
	
	# except e:
def signpage(request):
	return render(request,'signup.html',{'title':'Sign Page','is_reg':True})

def loginpage(request):
	return render(request,'signin.html',{'title':'Sign Page'})