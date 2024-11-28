from django import forms

from advertiserList.models import advertiserList


class advertiserListForm(forms.ModelForm):
    class Meta:
        model=advertiserList
        fields=('title','nickname')