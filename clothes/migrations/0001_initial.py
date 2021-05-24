# Generated by Django 3.2.3 on 2021-05-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genderSelection', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='Female', max_length=1)),
            ],
        ),
    ]