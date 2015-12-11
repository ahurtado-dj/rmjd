from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from oic.oic import Client
from oic.oauth2 import rndstr
from oic.oic.message import AuthorizationResponse
from oic.utils.authn.client import ClientSecretPost

import json

import logging
logger = logging.getLogger(__name__)


CLIENT__OAUTH2KEY = 'sP6Q8PhleQ_s7Ai7lv_EcHLhGXMa' 
CLIENT__OAUTH2SECRET = 'lEs6BLbJMo7Ggw95IpEFYAOpB_Qa' 
WSO2IS__AUTHORIZATIONENDPOINT = 'https://190.184.205.151:9443/oauth2/authorize' 
WSO2IS__TOKENENDPOINT = 'https://190.184.205.151:9443/oauth2/token' 
CLIENT__REDIRECTURL = 'http://localhost:8000/auth/access_token_request/'


# implementation using FBV (function based views)

def home(request):
	logger.debug("starting auth...")
	context = {}
	return render(request, 'm_auth/home.html', context)


def authorization_request(request):
	cliente = Client()
	hapax = rndstr()
	state = rndstr()
	params = {
		"authorization_endpoint": WSO2IS__AUTHORIZATIONENDPOINT,
		"client_id": CLIENT__OAUTH2KEY,
		"response_type": "code",
		"scope": ["openid"],
		"nonce": hapax,
		"redirect_uri": CLIENT__REDIRECTURL
	}
	result = cliente.do_authorization_request(
		state=state,
		request_args=params
	)
	logger.debug(" auth (1) %s" % (state))
	request.session['state'] = state
	return HttpResponseRedirect(result.headers['location'])


def access_token_request(request):
	client = Client(
		client_id=CLIENT__OAUTH2KEY,
		client_authn_method={"client_secret_post": ClientSecretPost}
	)
	raw_response = json.dumps(dict(request.GET))
	aresp = client.parse_response(AuthorizationResponse, info=raw_response) #, sformat="urlencoded")
	arespdata_state = aresp['state']
	sessiondata_state = request.session['state']
	logger.debug(" auth (2) %s" % (arespdata_state))

	if arespdata_state == sessiondata_state:
		code = aresp['code']
		params = {
			"token_endpoint": WSO2IS__TOKENENDPOINT,
			"code": code,
			"client_id": CLIENT__OAUTH2KEY,
			"client_secret": CLIENT__OAUTH2SECRET,
			"redirect_uri": CLIENT__REDIRECTURL
		}
		result = client.do_access_token_request(
			scope = ["openid"],
			state = arespdata_state,
			request_args = params,
			authn_method = "client_secret_post"
		)

		user_data = result['id_token']['sub']
		document_id = user_data[:user_data.find('@')]

		logger.debug(" auth (3) %s [doc=%s]" % (arespdata_state, document_id))

		return HttpResponse("User authenticated {}".format(document_id))
	else:
		return HttpResponse("Error: invalid parameters sent to authorization endpoint.")