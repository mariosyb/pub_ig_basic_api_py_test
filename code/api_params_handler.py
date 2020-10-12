from api_calls_handler import getInstagramInfo


igInfo = getInstagramInfo()


def getShortLivedAccessTokenEndpointParams(instagramCode):
    # curl -X POST \ https://api.instagram.com/oauth/access_token
    #  \ -F client_id={app-id} \ -F client_secret={app-secret}
    #  \ -F grant_type=authorization_code \ -F redirect_uri={redirect-uri}
    #  \ -F code={code}

    params = dict()
    params['client_id'] = igInfo['instagram_app_id']
    params['client_secret'] = igInfo['instagram_app_secret']
    params['grant_type'] = 'authorization_code'
    params['redirect_uri'] = igInfo['instagram_app_redirect_uri']
    params['code'] = instagramCode

    return params


def getLongLivedAccessTokenEndpointParams(shortLivedAccessToken):
    # curl -i -X GET "https://graph.instagram.com/access_token
    #  ?grant_type=ig_exchange_token
    #  &client_secret={instagram-app-secret}
    #  &access_token={short-lived-access-token}"

    params = dict()
    params['grant_type'] = 'ig_exchange_token'
    params['client_secret'] = igInfo['instagram_app_secret']
    params['access_token'] = shortLivedAccessToken

    return params


def refreshAccessTokenEndpointParams(longLivedAccessToken):
    # curl -i -X GET "https://graph.instagram.com/refresh_access_token
    #  ?grant_type=ig_refresh_token
    #  &access_token={long-lived-access-token}"

    params = dict()
    params['grant_type'] = 'ig_refresh_token'
    params['access_token'] = longLivedAccessToken

    return params


"""
    las llamadas que reciben listas de campos: {fields}
    podrian recibirlos como argumentos como futura mejora
"""


def getUserNodeEndpointParams(accessToken):
    # https://graph.instagram.com/me
    # GET /me?fields={fields}&access_token={access-token}

    params = dict()
    params['fields'] = 'id,username,account_type'  # una lista separada por comas de los campos de usuario que deseas recibir
    params['access_token'] = accessToken

    return params


def getUserMediaElementsEndpointParams(accessToken):
    # GET /me/media?fields={fields}&access_token={access-token}
    # https://graph.instagram.com/me/media

    params = dict()
    params['fields'] = 'id,username,caption,media_type,media_url,timestamp'  # con una lista separada por comas de los campos de elementos multimedia que deseas recibir
    params['access_token'] = accessToken

    return params


def getMediaNodeEndpointParams(accessToken):
    # GET /{media-id}?fields={fields}&access_token={access-token}
    # https://graph.instagram.com/17895695668004550 -> id del elemento en la url

    params = dict()
    params['fields'] = 'id,username,caption,media_type,media_url,timestamp,permalink'  # con una lista separada por comas de los campos de elementos multimedia que deseas recibir
    params['access_token'] = accessToken

    return params


def getMediaAlbumEndpointParams(accessToken, fields):
    # GET /{media-id}/children?fields={fields}&access_token={access-token}
    #  'https://graph.instagram.com/17896450804038745/children?access_token=IGQVJ' -> id del elemento en la url
    # en este request se pueden omitir los campos: {fields} si solo se quiere obtener los id de los elementos del album

    params = dict()
    if not (fields is None):
        params['fields'] = fields
    params['access_token'] = accessToken

    return params
