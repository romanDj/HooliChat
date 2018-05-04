# Generated by Django 2.0.4 on 2018-05-04 06:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0003_conversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='conversation',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 9, 21, 21, 304293), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='participants',
            name='convers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Conversation'),
        ),
        migrations.AddField(
            model_name='participants',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]