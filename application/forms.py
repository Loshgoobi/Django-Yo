from django import forms
from application.models import Cards


class ContactForm(forms.Form):
    username = forms.CharField(label='user name', max_length=30)
    password = forms.CharField(label='pass word', max_length=30)
    firstname = forms.CharField(label='first name', max_length=30)
    lastname = forms.CharField(label='last name', max_length=30)

    def __str__(self):
        return self.name

    #sujet = forms.CharField(max_length=100)
    #message = forms.CharField(widget=forms.Textarea)
    #envoyeur = forms.EmailField(label="Votre adresse mail")
    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


class CardForm(forms.ModelForm):
    class Meta:
        model = Cards
        exclude = []
        #forms.Select(choices=TITLE_CHOICES)