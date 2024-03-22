from django.contrib.auth import get_user_model
from django.db import models
from djmoney.models.fields import MoneyField

User = get_user_model()


class Сategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = ...

    def __str__(self):
        return self.title


class Payment(models.Model):
    amount = MoneyField(
        max_digits=14, decimal_places=2, default_currency='RUB'
    )
    date = models.DateTimeField(
        'Дата оплаты', auto_now_add=True, db_index=True
    )


class Subscription(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL,
        related_name="subscription", blank=True, null=True
    )
    category = models.ForeignKey(
        Сategory, on_delete=models.SET_NULL,
        related_name="subscription", blank=True, null=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = MoneyField(
        max_digits=14, decimal_places=2, default_currency='RUB'
    )
    period = ...

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"  # !
    )
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE, related_name="subscription"  # !
    )
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="follower"  # !
    )
    date_subscription = models.DateTimeField(
        'Дата начала', auto_now_add=True, db_index=True
    )
    date_payment = models.DateTimeField(
        'Дата списания', auto_now_add=True, db_index=True
    )
    status = ...

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "subscription"], name="unique_follow"
            )
        ]


class Cashback(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"  # !
    )
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="follower"  # !
    )
    amount = MoneyField(
        max_digits=14, decimal_places=2, default_currency='RUB'
    )
    status = ...
    balance = MoneyField(
        max_digits=14, decimal_places=2, default_currency='RUB'
    )
    interest_rate = ...
