from django import forms

class Email_form(forms.Form):

    email = forms.EmailField()

    def __str__(self):
        return self.email

        