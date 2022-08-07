from  django import forms
from .models import Comment


class CommentUpdateForm(forms.ModelForm):
	message = forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Message......."}), max_length = 800)
	class Meta:
		model=Comment
		fields=['message']