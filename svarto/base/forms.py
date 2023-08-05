from django import forms

class ContactForm(forms.Form):
    txtName = forms.CharField(label='Your Name', max_length=100)
    txtEmail = forms.EmailField(label='Your Email')
    txtPhone = forms.CharField(label='Your Phone Number', max_length=20)
    txtMsg = forms.CharField(label='Your Message', widget=forms.Textarea)
