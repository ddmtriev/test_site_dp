# Generated by Django 4.2.6 on 2023-10-27 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=150)),
                ('oblast', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')])),
                ('age', models.IntegerField()),
                ('organization', models.CharField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('test_type', models.CharField(choices=[('1', 'Пользовательский'), ('2', 'Контрольный')], max_length=300)),
                ('slug', models.SlugField(max_length=150, null=True, unique=True, verbose_name='URL')),
                ('test_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='test_main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=300)),
                ('answer1', models.CharField(max_length=150)),
                ('answer2', models.CharField(max_length=150)),
                ('answer3', models.CharField(max_length=150)),
                ('answer4', models.CharField(max_length=150)),
                ('is_correct', models.CharField(choices=[('1', models.CharField(max_length=150)), ('2', models.CharField(max_length=150)), ('3', models.CharField(max_length=150)), ('4', models.CharField(max_length=150))], max_length=150)),
                ('user_answer', models.CharField(blank=True, choices=[('1', models.CharField(max_length=150)), ('2', models.CharField(max_length=150)), ('3', models.CharField(max_length=150)), ('4', models.CharField(max_length=150))], max_length=150, null=True)),
                ('test_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_main.test')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_answer', models.CharField(max_length=150)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_main.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_main.user')),
            ],
        ),
    ]
