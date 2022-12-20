# Generated by Django 4.0.1 on 2022-11-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('authour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.useracounts')),
            ],
        ),
    ]
