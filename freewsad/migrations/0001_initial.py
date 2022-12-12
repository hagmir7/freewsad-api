# Generated by Django 4.0.5 on 2022-08-24 15:39

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='BOOK ')),
                ('author', models.CharField(blank=True, max_length=50, null=True, verbose_name='Author ')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Page Number ')),
                ('book_type', models.CharField(default='PDF', max_length=30, verbose_name='Book Type ')),
                ('image', models.ImageField(upload_to='books_Image/', verbose_name='Image ')),
                ('link', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Link')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description ')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Read Book')),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, upload_to='books/', verbose_name='File')),
                ('is_public', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='AdminImage/')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body ')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_block', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', models.CharField(blank=True, max_length=150, null=True)),
                ('valid', models.BooleanField(blank=True, default=False, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('catgory', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Template Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('olde_price', models.FloatField(blank=True, null=True, verbose_name='Olde Price')),
                ('demo', models.CharField(max_length=1000, verbose_name='Demo Link')),
                ('file', models.FileField(upload_to='Templates', verbose_name='Template File')),
                ('tags', models.CharField(blank=True, max_length=166, verbose_name='Tags')),
                ('body', models.TextField(default=' ', verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('add_to_cart', models.ManyToManyField(related_name='template_add_to_catd', to=settings.AUTH_USER_MODEL, verbose_name='Cart')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='TempletsImages')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TemplatesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateTols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='TemplateImageTools')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='TemplatesCategoryImages', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freewsad.template')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='template',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freewsad.templatescategory', verbose_name='Template Category'),
        ),
        migrations.AddField(
            model_name='template',
            name='image',
            field=models.ManyToManyField(related_name='templateImage', to='freewsad.templateimages', verbose_name='Templates Images'),
        ),
        migrations.AddField(
            model_name='template',
            name='tols',
            field=models.ManyToManyField(blank=True, related_name='template_tols', to='freewsad.templatetols'),
        ),
        migrations.AddField(
            model_name='template',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Template'),
        ),
        migrations.CreateModel(
            name='PostList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name ')),
                ('description', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(default='default-post.png', upload_to='play_list_cover')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=400)),
                ('date', models.DateTimeField(auto_now=True)),
                ('updat', models.DateTimeField(auto_now_add=True)),
                ('like', models.ManyToManyField(related_name='like_comment', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='freewsad.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.language')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='freewsad.postcategory'),
        ),
        migrations.AddField(
            model_name='post',
            name='ip_like',
            field=models.ManyToManyField(blank=True, related_name='ip_like', to='freewsad.ipmodel'),
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.language'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_post',
            field=models.ManyToManyField(related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.postlist'),
        ),
        migrations.AddField(
            model_name='post',
            name='save_post',
            field=models.ManyToManyField(related_name='save_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='freewsad.ipmodel'),
        ),
        migrations.CreateModel(
            name='CommentBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_book', to='freewsad.book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name ')),
                ('description', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(default='default-post.png', upload_to='play_list_cover')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.language')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.language')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.bookcategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.language'),
        ),
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.ManyToManyField(related_name='book_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freewsad.booklist'),
        ),
        migrations.AddField(
            model_name='book',
            name='save_book',
            field=models.ManyToManyField(related_name='book_save', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='book_viws', to='freewsad.ipmodel'),
        ),
    ]
