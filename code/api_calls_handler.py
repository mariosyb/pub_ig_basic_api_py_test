import requests
import json
import enum

IG_APP_ID = '<YOUR_APP_ID>'
IG_APP_SECRET = '<YOUR_APP_SECRET>'
IG_BASIC_DOMAIN = 'https://api.instagram.com'
IG_GRAPH_DOMAIN = 'https://graph.instagram.com'


class HttpMethods(enum.Enum):
    get = 'GET'
    post = 'POST'


def getInstagramInfo():
    igInfo = dict()
    igInfo['instagram_app_id'] = IG_APP_ID
    igInfo['instagram_app_secret'] = IG_APP_SECRET
    igInfo['instagram_app_redirect_uri'] = 'https://mariosyb.github.io/ig_basic_api_page/'
    igInfo['short_lived_token_base_uri'] = IG_BASIC_DOMAIN + '/oauth/access_token'
    igInfo['long_lived_token_base_uri'] = IG_GRAPH_DOMAIN + '/access_token'
    igInfo['refresh_token_base_uri'] = IG_GRAPH_DOMAIN + '/refresh_access_token'
    igInfo['user_node_base_uri'] = IG_GRAPH_DOMAIN + '/me'
    igInfo['user_media_elements_base_uri'] = IG_GRAPH_DOMAIN + '/me/media'

    return igInfo


def makeApiCall(url, params, method):
    if 'GET' == method:
        data = requests.get(url, params)
    elif 'POST' == method:
        data = requests.post(url, params)
    else:
        print(f'ERROR: not supported method: {method}')
        return

    custonResponse = dict()
    custonResponse['url'] = url
    custonResponse['request_params_raw'] = params
    custonResponse['request_params_pretty'] = json.dumps(params, indent=4)  # convierte el python(dic) a json
    custonResponse['response_data_raw'] = json.loads(data.content)  # convierte el json a python(dic)
    custonResponse['response_data_pretty'] = json.dumps(custonResponse['response_data_raw'], indent=4)

    return custonResponse


def printApiResponse(custonResponse):
    print('\nURL:')
    print(custonResponse['url'])
    print('\nParametros usados:')
    print(custonResponse['request_params_pretty'])
    print('\nRespuesta del api de Instagram:')
    print(custonResponse['response_data_pretty'])
    print('\n=======================')
