from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

import requests
from git_gg.settings import CLIENT_ID, CLIENT_SECRET


@api_view(['GET'])
def get_code(request):
	code = ""
	if 'code' in request.GET:
		code = request.GET['code']

	github_url = 'https://github.com/login/oauth/access_token'
	params = {}
	params['client_id'] = CLIENT_ID
	params['client_secret'] = CLIENT_SECRET
	params['code'] = code
	response = requests.post(github_url, params=params)
	response = response.text.split('&')
	response_dict = {}
	for r in response:
		s = r.split('=')
		response_dict[s[0]] = s[1]
	status = 200
	if 'error' in response_dict:
		status = 400
	return Response(response_dict, status=status)
