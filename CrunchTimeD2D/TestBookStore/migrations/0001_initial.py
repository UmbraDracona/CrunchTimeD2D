# Generated by Django 3.0.3 on 2020-02-12 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('given_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OnixFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('isbn_13', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=100)),
                ('series_name', models.CharField(blank=True, max_length=100)),
                ('volume_no', models.CharField(blank=True, max_length=3)),
                ('description', models.TextField(blank=True)),
                ('book_format', models.CharField(blank=True, max_length=10)),
                ('price', models.CharField(blank=True, max_length=10)),
                ('release_date', models.DateTimeField(blank=True)),
                ('publisher', models.CharField(blank=True, max_length=100)),
                ('authors', models.ManyToManyField(blank=True, to='TestBookStore.Author')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, to='TestBookStore.Book'),
        ),
    ]