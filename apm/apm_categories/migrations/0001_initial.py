# Generated by Django 5.0.6 on 2024-07-11 07:42

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ASHPenserCategories',
            fields=[
                ('category_data', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('category_type', models.CharField(blank=True, choices=[('Incomes', 'Incomes'), ('Expense', 'Expenses')], max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ashpenser_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CategoriesData',
                'db_table': 'categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='ASHPenserPaymentMethod',
            fields=[
                ('paymethod_data', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paymethod_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ashpenser_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_methods', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PaymentMethodsData',
                'db_table': 'payment_methods',
                'ordering': ('paymethod_name',),
            },
        ),
        migrations.CreateModel(
            name='ASHPenserSubCategories',
            fields=[
                ('subcategory_data', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subcategory_type', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ashpenser_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to=settings.AUTH_USER_MODEL)),
                ('category_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='apm_categories.ashpensercategories')),
            ],
            options={
                'verbose_name_plural': 'SubCategoriesData',
                'db_table': 'subcategories',
                'ordering': ('subcategory_name',),
            },
        ),
    ]
