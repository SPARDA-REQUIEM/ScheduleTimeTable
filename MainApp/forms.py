from django import forms
from .models import facultyMember

class facultyMemberForm(forms.ModelForm):
    class Meta:
        model = facultyMember
        fields = '__all__'