import requests
import json
from .user import User


class HabaticaClient(object):
    """Base class for Habatica API access"""

    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token

    def fetch_json(self, uri_path, http_method="GET", headers=None, query_params=None, post_args=None):
        """

        :param uri_path:
        :param http_method:
        :param headers:
        :param query_params:
        :param post_args:
        :return:
        """
        if headers is None:
            headers = {}
        if query_params is None:
            query_params = {}
        if post_args is None:
            post_args = {}
        data = None

        if http_method in ("POST", "PUT", "DELETE"):
            headers['Content-Type'] = 'application/json; charset=utf-8'

        headers['Accept'] = 'application/json'

        headers['x-api-user'] = self.api_key
        headers['x-api-key'] = self.api_token

        if uri_path[0] == '/':
            uri_path = uri_path[1:]
        url = 'https://habitica.com/api/v3/%s' % uri_path

        # perform the HTTP requests, if possible uses OAuth authentication
        data = json.dumps(post_args)
        response = requests.request(http_method, url, params=query_params,
                                    headers=headers, data=data)

        if response.status_code == 401:
            # TODO:Сделать нормальную обработку ошибок
            pass
            # raise Unauthorized("%s at %s" % (response.text, url), response)
        if response.status_code != 200:
            # TODO:Сделать нормальную обработку ошибок
            pass
            # raise ResourceUnavailable("%s at %s" % (response.text, url), response)

        return response.json()

    def get_user(self):
        obj = self.fetch_json('/user')
        return User.from_json(self, json_obj=obj)
