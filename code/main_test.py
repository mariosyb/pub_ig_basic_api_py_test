from api_calls_handler import getInstagramInfo
from api_calls_handler import printApiResponse
from api_calls_handler import makeApiCall
from api_calls_handler import HttpMethods
from api_params_handler import getShortLivedAccessTokenEndpointParams
from api_params_handler import getLongLivedAccessTokenEndpointParams
from api_params_handler import refreshAccessTokenEndpointParams
from api_params_handler import getUserNodeEndpointParams
from api_params_handler import getUserMediaElementsEndpointParams
from api_params_handler import getMediaNodeEndpointParams
from api_params_handler import getMediaAlbumEndpointParams

# replace for your exchange code
EXCHANGE_CODE = (
    'AQANUxxNNEye27fkBn3G1GbXD2E0sOIWejVEMjmctsXPIku-c6WtDf1XAUQSOzU7mdJ8RhoObp9n_L2HtFI7MxgHeVxNfKo' +
    'p4LNt0ef5BYXdFIhXvZYsQWmmhZqEddaQrXCvPA5dGuEqNzagq7vDmHJFeaW3MzgeGhRkBOsSRCNOmDZfO01VKixustZCIJraW0XcxYi4_wg1wsPCJX8QWTNY4xkq5CaDSvzdpwTIYTslbA'
)

# replace for your long loved token
LONG_LIVED_TOKEN = (
    'IGQVJVYVdzcVZA2bVhmbFkwX1M2MlRKc0c2b05tQWFoSDFqQWRDWHEta0xLQ0Q3Y2M' +
    'xUm5kMGFqSHdPa19ha2VuVW5Sd3JCWmMycWh3ZAXVoSUZAwbjQtcEpJa1hNVkFmd0MxU3JCRDBn'
)

igInfo = getInstagramInfo()
shortTokenResponse = None
userMediaRespose = None


def getToken():
    # obtener token simple
    global shortTokenResponse
    shortTokenResponse = makeApiCall(
        igInfo['short_lived_token_base_uri'],
        getShortLivedAccessTokenEndpointParams(EXCHANGE_CODE),
        HttpMethods.post.value
        )

    printApiResponse(shortTokenResponse)


def exchangeToken():
    # cambiar token simple por el token de larga duracion
    shortLivedToken = shortTokenResponse['response_data_raw']['access_token']  # diccionario anidado

    longTokenResponse = makeApiCall(
        igInfo['long_lived_token_base_uri'],
        getLongLivedAccessTokenEndpointParams(shortLivedToken),
        HttpMethods.get.value
    )

    printApiResponse(longTokenResponse)


def refreshToken():
    refreshTokenResponse = makeApiCall(
        igInfo['refresh_token_base_uri'],
        refreshAccessTokenEndpointParams(LONG_LIVED_TOKEN),
        HttpMethods.get.value
    )

    printApiResponse(refreshTokenResponse)


def getUserNode():
    userNodeResponse = makeApiCall(
        igInfo['user_node_base_uri'],
        getUserNodeEndpointParams(LONG_LIVED_TOKEN),
        HttpMethods.get.value
    )

    printApiResponse(userNodeResponse)


def getUserMediaElements():
    global userMediaRespose
    userMediaRespose = makeApiCall(
        igInfo['user_media_elements_base_uri'],
        getUserMediaElementsEndpointParams(LONG_LIVED_TOKEN),
        HttpMethods.get.value
    )

    printApiResponse(userMediaRespose)


def getMediaNodeInfo():
    mediaElementId = userMediaRespose['response_data_raw']['data'][0]['id']
    mediaNodeResponse = makeApiCall(
        'https://graph.instagram.com/' + mediaElementId,
        getMediaNodeEndpointParams(LONG_LIVED_TOKEN),
        HttpMethods.get.value
    )

    printApiResponse(mediaNodeResponse)


def getMediaAlbum(albumId, fields):
    # fields puede viajar 'None'
    mediaAlbumrResponse = makeApiCall(
        f'https://graph.instagram.com/{albumId}/children',
        getMediaAlbumEndpointParams(LONG_LIVED_TOKEN, fields),
        HttpMethods.get.value
    )

    printApiResponse(mediaAlbumrResponse)


# getToken()
# exchangeToken()
# refreshToken()
# getUserNode()
# getUserMediaElements()
# getMediaNodeInfo()
