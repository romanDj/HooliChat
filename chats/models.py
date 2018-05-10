import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PrivateMessages(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
	message_text = models.CharField(max_length=1000)
	def  __str__(self):
		return str(str(self.id)+": from "+str(self.sender)+' to '+str(self.recipient))

class Conversation(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
	def __str__(self):
		return self.name

class Participants(models.Model):
	convers = models.ForeignKey(Conversation, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.convers + ' - ' + self.user

class ConversMessages(models.Model):
	sender = models.ForeignKey(Participants, on_delete=models.CASCADE)
	message_text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
	def __str__(self):
		return self.sender + ' - ' + self.pub_date


		