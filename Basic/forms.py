from allauth.account.forms import SignupForm
from django import forms
from . models import Events,Booking

class BusinessSignupForm(SignupForm):
    license_data = forms.CharField(max_length=264)
    license_file = forms.FileField()


    def save(self, request):
        user = super(BusinessSignupForm, self).save(request)
        user.license_data = self.cleaned_data.get('license_data')
        user.license_file = self.cleaned_data.get('license_file')
        user.is_Service_provider = True
        user.save()
        return user


#class LicenseVerificationForm(forms.Form):
    #license_information = forms.Textarea(blank=False)
class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title','description', 'thumbnail','category','keywords','price')

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date',)


