from django import forms
    
class CommentForm(forms.Form):
    user_comment = forms.CharField(max_length=256, help_text="Enter comment (max: 256 chars)")

    # def clean_comment(self):
    #     good_comment = self.cleaned_data('user_comment')
    #     good_comment = str(good_comment)
    #     return good_comment