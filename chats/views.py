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
from django.db.models.query import QuerySet
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
	arr_chat = []
	#если в url есть номер то смотрим есть ли чат с ним 
	if interl_id is not None:
		interlocutors = PrivateMessages.objects.filter(Q(sender=request.user.id, recipient=interl_id) | Q(sender=interl_id , recipient=request.user.id)).values_list('sender', 'recipient').distinct()
		#получаем имя пользователя
		if interlocutors is not None:
			getUserNew = User.objects.get(id=interl_id)

	#если номера нет выгружаем все чаты
	else:
		interlocutors = PrivateMessages.objects.filter(Q(sender=request.user.id) | Q(recipient=request.user.id)).values_list('sender','recipient').distinct()
		

	interlocutors = list(interlocutors)
	print(interlocutors)
	for i,arr in enumerate(interlocutors):
		tmp = list(arr)
		tmp.reverse()
		print('TMP - '+str(tmp))
		for arr2 in interlocutors:
			if tuple(tmp) == arr2:
				interlocutors.pop(i)
	for tupl in interlocutors:
		if tupl[0] == request.user.id:
			arr_chat.append({
				'username': User.objects.get(id=tupl[1]),
			})
		else:
			arr_chat.append({
				'username': User.objects.get(id=tupl[0]),
			})
	print(arr_chat)
	return render(request, 'chats/index.html', {'page' : 'chats', 'interlocutors' : arr_chat, 'getUser' : getUserNew })

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

