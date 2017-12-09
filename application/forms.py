from django import forms
from application.models import Cards


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)

    #sujet = forms.CharField(max_length=100)
    #message = forms.CharField(widget=forms.Textarea)
    #envoyeur = forms.EmailField(label="Votre adresse mail")
    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


class Card(forms.ModelForm):
    class Meta:
        model = Cards
        exclude = []