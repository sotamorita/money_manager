from django import forms
from .models import JournalentryModel


# creating a form
class JournalentryForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = JournalentryModel

        # specify fields to be used
        fields = [
            "date",
            "dr_account",
            "dr_price",
            "dr_class",
            "cr_account",
            "cr_price",
            "cr_class",
        ]
