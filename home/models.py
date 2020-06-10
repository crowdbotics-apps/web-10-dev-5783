from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    ytgfhgfkhgf = models.OneToOneField(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_ytgfhgfkhgf",
    )
    hgfkhfkhf = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_hgfkhfkhf",
    )
    ghfkjfjf = models.ManyToManyField(
        "home.HomePage", blank=True, related_name="customtext_ghfkjfjf",
    )
    mhgfkhgfkh = models.BigIntegerField(null=True, blank=True,)
    hgfjhgfhgf = models.BigIntegerField(null=True, blank=True,)
    kjhlkjhkljh = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_kjhlkjhkljh",
    )
    sgdagdasd = models.ManyToManyField(
        "home.CustomText", blank=True, related_name="customtext_sgdagdasd",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
