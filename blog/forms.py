from django import forms


class PubBlogForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2)
    content = forms.CharField(widget=forms.Textarea)
    category = forms.IntegerField()