# Generated by Django 5.0.3 on 2024-03-19 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0003_cheese_pizza_pizzatype_toppings_delete_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cheese",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="customers.cheese",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customers.order",
                    ),
                ),
                (
                    "pizza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customers.pizza",
                    ),
                ),
                (
                    "pizzaType",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="customers.pizzatype",
                    ),
                ),
                ("toppings", models.ManyToManyField(to="customers.toppings")),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="pizzas",
            field=models.ManyToManyField(
                through="customers.OrderDetail", to="customers.pizza"
            ),
        ),
    ]
