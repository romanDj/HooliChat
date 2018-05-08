import math, datetime
import rsa
import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import *
from .models import *

# Create your views here.
def index(request):
	form = UserForm()
	data = {'myform': form}
	return render(request, 'chats/auth.html', data)

def sigin(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			log = form.cleaned_data['login']
			pas = form.cleaned_data['password']
			user = authenticate(username=log, password=pas)
			if user is not None:
				if user.is_active:
					login(request, user)
				return redirect('mychats')
			else:
				data = {'myform':form, 'error': "Неправильный логин или пароль."}
				return render(request, 'chats/auth.html', data)
	

def mychats(request, interl_id=None):
	getUserNew = None
	if interl_id is not None:
		interlocutors = PrivateMessages.objects.filter(Q(sender=request.user.id, recipient=interl_id) | Q(sender=interl_id , recipient=request.user.id))
		if interlocutors is not None:
			getUserNew = User.objects.get(id=interl_id)
	interlocutors = PrivateMessages.objects.filter(Q(sender=request.user.id) | Q(recipient=request.user.id))
	return render(request, 'chats/index.html', {'page' : 'chats', 'interlocutors' : interlocutors, 'getUser' : getUserNew })

def profil(request):
	return render(request, 'chats/myroom.html')

def logoutDef(request):
	logout(request)
	return redirect('index')

def users(request):
	loadUsers = User.objects.all()
	return render(request, 'chats/users.html', {'users' : loadUsers})

def registration(request):
	RegisterFormView(request)

def lol(request):
	(pubkey, privkey) = rsa.newkeys(512)
	message = str.encode('Привеееет')
	# шифруе
	crypto = rsa.encrypt(message, pubkey)
	print(crypto)
	#расшифровываем
	message = rsa.decrypt(crypto, privkey)
	print(message.decode())
	return HttpResponse(message)

def add_message(request):
	print('сообщение получено')
	if request.method == 'GET':
		getMe = User.objects.get(id = request.user.id)
		getFriend = User.objects.get(id = request.GET['recipient'])
		newMess = PrivateMessages(sender = getMe, recipient = getFriend, message_text = request.GET['text'])
		newMess.save()
		print('Добавлено')

	return HttpResponse('lollol')

