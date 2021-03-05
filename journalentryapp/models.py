from django.db import models

# Create your models here.

CLASS = (
    ('assets', '資産'),
    ('liabilities', '負債'),
    ('equity', '純資産'),
    ('expenses', '費用'),
    ('revenue', '収益'),
)
class JournalentryModel(models.Model):
    date = models.DateField()
    dr_account = models.CharField(max_length=30)
    dr_price = models.IntegerField()
    dr_class = models.CharField(
        max_length=30,
        choices=CLASS,
    )
    cr_account = models.CharField(max_length=30)
    cr_price = models.IntegerField()
    cr_class = models.CharField(
        max_length=30,
        choices=CLASS,
    )

    def __str__(self):
         return str(self.date) + ':' + self.dr_account + ' ' +  self.cr_account
