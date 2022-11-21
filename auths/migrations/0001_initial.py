# Generated by Django 4.0.5 on 2022-07-13 06:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('image', models.ImageField(null=True, upload_to='products', verbose_name='Фотография')),
                ('image2', models.ImageField(null=True, upload_to='products', verbose_name='Фотография')),
                ('image3', models.ImageField(null=True, upload_to='products', verbose_name='Фотография')),
                ('reiting', models.FloatField(default=0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта/Логин')),
                ('number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус менеджера')),
                ('data_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('hobbies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auths.hobbies')),
                ('hobbies2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auths.hobbies2')),
                ('hobbies3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auths.hobbies3')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('data_joined',),
            },
        ),
    ]
