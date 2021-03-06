# Generated by Django 2.0.4 on 2018-05-04 06:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20180504_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 5, 4, 9, 26, 32, 361748), verbose_name='date published')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Participants')),
            ],
        ),
        migrations.AlterField(
            model_name='conversation',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 9, 26, 32, 360747), verbose_name='date published'),
        ),
    ]
