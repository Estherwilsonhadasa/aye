from django import forms
# from django.conf import settings
# from watson_developer_cloud import ConversationV1

class ChatForm(forms.Form):
	message = forms.CharField(max_length=100, required=True)

	# def ask_watson(self):
	# 	text = self.cleaned_data['message']