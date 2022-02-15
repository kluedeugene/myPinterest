from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start', #text-left가 start로 바뀌었다(부트스트랩5)
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)        #create에서 project필드관련 없어도 작성가능하게

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']

