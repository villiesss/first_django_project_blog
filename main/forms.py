from django import forms


class PostForm(forms.Form):
    author = forms.CharField(max_length=50, label='Author')
    title = forms.CharField(max_length=200, label='3arOJIoBoK')
    text = forms.CharField(widget=forms.Textarea, label="Post Text")