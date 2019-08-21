# Generated by Django 2.2.3 on 2019-07-27 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pubDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=1000)),
                ('imageSecond', models.ImageField(upload_to='images/')),
                ('imageFirst', models.ImageField(upload_to='images/')),
                ('UserType', models.CharField(max_length=30)),
                ('authorName', models.CharField(max_length=30)),
                ('blogCategory', models.CharField(max_length=30)),
                ('refrenceLinks', models.CharField(max_length=30)),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]