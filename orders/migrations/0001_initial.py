# Generated by Django 4.1.1 on 2022-10-11 20:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        editable=False,
                                        help_text='Unique ID',
                                        primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(default='Description', help_text='Description', max_length=255)),
                ('amount',
                 models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('code', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('discount_type', models.SmallIntegerField(default=0, verbose_name=[(0, 'Value'), (1, 'Percent')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True,
                                        serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(default='Description', help_text='Description', max_length=255)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='orders.discount')),
                ('products', models.ManyToManyField(to='items.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
