# Generated by Django 2.1.5 on 2019-01-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursion_website', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('1', 'Superuser'), ('2', 'Member'), ('3', 'User')], default='3', max_length=50),
        ),
    ]