from django.shortcuts import render
from django.conf import settings
from watson_developer_cloud import ConversationV1
from .forms import ChatForm
import json 
from django.http import JsonResponse


# Create your views here.

def dialogue_json(request):
	conversation = ConversationV1(
   	username = settings.USERNAME,
	password = settings.PASSWORD,
    version='2018-02-16'
)

	response = conversation.get_dialog_node(
	    workspace_id = 'db92f9fa-5fcc-493c-ba9e-3ded910924da',
	    dialog_node = 'Welcome'
	)

	return JsonResponse(response)


def get_dialogue(request):
	conversation = ConversationV1(
   	username = settings.USERNAME,
	password = settings.PASSWORD,
    version='2018-02-16'
	)

	response={}
	if request.method == 'POST':
		form = ChatForm(request.POST)
		if form.is_valid():
			response = conversation.message(
				workspace_id = settings.WORKSPACE_ID,
				input = {
					'text':	form.cleaned_data['message']
				}
				)
			
		response['message'] = json.dumps(response['output']['text'], indent=2)
		return JsonResponse(response)

	else:
		form = ChatForm()



	response = conversation.get_dialog_node(
	    workspace_id = 'db92f9fa-5fcc-493c-ba9e-3ded910924da',
	    dialog_node = 'Welcome'
	)

	print(json.dumps(response, indent=2 ,))
	return render(request,'get_dialogue.html',{'form': form})


def index(request):
	return render(request,'index.html',{})


def home(request):
	conversation = ConversationV1(
   	username = settings.USERNAME,
	password = settings.PASSWORD,
    version='2018-02-16'
	)

	response={}
	if request.method == 'POST':
		form = ChatForm(request.POST)
		if form.is_valid():
			response = conversation.message(
				workspace_id = settings.WORKSPACE_ID,
				input = {
					'text':	form.cleaned_data['message']
				}
				)
			
		response['message'] = json.dumps(response['output']['text'], indent=2)
		return JsonResponse(response)

	else:
		form = ChatForm()



	response = conversation.get_dialog_node(
	    workspace_id = 'db92f9fa-5fcc-493c-ba9e-3ded910924da',
	    dialog_node = 'Welcome'
	)

	print(json.dumps(response, indent=2 ,))
	return render(request,'home.html',{'form': form})
	# return render(request,'home.html',{})