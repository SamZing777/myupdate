# Generated by Django 3.1 on 2020-08-24 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('matter', models.CharField(choices=[('Campaign', 'CAMPAIGN'), ('Emergency', 'EMERGENCY'), ('Good news', 'GOOD NEWS'), ('Rumour', 'RUMOUR'), ('Story', 'STORY')], default='Good news', max_length=10)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('informant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]