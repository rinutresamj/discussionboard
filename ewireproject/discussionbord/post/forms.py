from django import forms
from .models import Post
class UserProfileForm(forms.ModelForm):
    # Define your form fields and widgets
    #department = forms.ModelChoiceField(queryset=Department.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'description', 'tags', 'publication_date', 'is_published']
        widgets = {
            'tags': forms.CheckboxSelectMultiple

        }