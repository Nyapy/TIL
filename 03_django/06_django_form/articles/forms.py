from django import forms
from . models import Article, Comment

# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         # fields = '__all__'
#         fields = ('title', 'content',)
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={
#                     'class':'my-title',
#                     'placeholder':'Enter the title!',
#                     }
#             )
#         }

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title!',
            }
        ))
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows':5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
    comment = forms.TextInput(
        attrs={
            'class':'my-comment',
            'placeholder':'댓글입력 ㄱ'
        }
    )
    class Meta:
        model = Comment
        fields = ('comment',)


 # class ArticleForm(forms.Form):
    # title = forms.CharField(
    #     max_length = 20,
    #     label= '제목',
    #     widget= forms.TextInput(
    #         attrs={
    #             'class': 'my-title',
    #             'placeholder': 'Enter the title!',
    #         },
    #     )
    # )
    # content = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'my-content',
    #             'placeholder' : 'Enter the content!',
    #             'rows':5,
    #             'cols':50,
    #         }
    #     )
    # )