from django import forms

# our new form
class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    contact_number = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    attachment = forms.ImageField(required=False)



    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = "Shkruaj kodin e produktit:"
        self.fields['from_email'].label = "Shkruani email-in tuaj:"
        self.fields['message'].label = "Beni porosine tuaj"
        self.fields['attachment'].label = "Foto te cilen do te personalizoni"
        self.fields['contact_number'].label = "Shkruani numrin tuaj te kontaktit"
