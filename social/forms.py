from django import forms
from .models import SocialPost, SocialComment


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
        'rows': '3',
        'placeholder': 'Comentar algo...'
    }), required=False)  # Changed to required=False

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
    }), required=False)

    class Meta:
        model = SocialPost
        fields = ['body', 'image']

    def clean(self):
        cleaned_data = super().clean()
        body = cleaned_data.get('body')
        image = cleaned_data.get('image')

        #Validar que se proporcione al menos texto o imagen.
        if not body and not image:
            raise forms.ValidationError("Debe proporcionar un comentario de texto o una imagen..")

        return cleaned_data



class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Comenta Algo...'
            }),
        required=True
        )

    class Meta:
        model=SocialComment
        fields=['comment']
   
    
class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '3',
            'placeholder': 'Comentar algo...'
            }),
        )