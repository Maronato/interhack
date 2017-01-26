from django.db import models

# Create your models here.


choices = (
    ('UCAMP', 'Unicamp'),
    ('USPSP', 'USP - São Paulo'),
    ('USPSC', 'USP - São Carlos'),
    ('UFSCA', 'UFSCAR'),
    ('OUTRA', 'Outra'),
)


class Registree(models.Model):

    name = models.CharField(max_length=84, default='')
    email = models.EmailField(unique=True)
    university = models.CharField(choices=choices, max_length=5)
    other = models.CharField(max_length=42, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    chimp_id = models.CharField(max_length=42, default='')
    referee = models.ForeignKey(
        "Registree",
        on_delete=models.CASCADE,
        related_name='references',
        null=True
    )
    status = models.CharField(max_length=42, default='pending')

    def __str__(self):
        return self.email
