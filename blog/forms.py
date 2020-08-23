from django import forms

from .models import Post
from .models import CV
from .models import CV2
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('author', 'Number', 'Email', 'Date_of_birth', 'Personal_Profile', 'Education', 'Employment_History', 'Achievements', 'Interests', 'Skills', 'References')

class CV2Form(forms.ModelForm):
    class Meta:
        model = CV2
        fields = ('author', 'Number', 'Email', 'Date_of_birth', 'Personal_Profile', 'Education', 'Employment_History', 'Achievements', 'Interests', 'Skills', 'References')
