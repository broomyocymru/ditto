import json
import urllib

import requests

import atlassian_password


class ConfluenceClient:
    def __init__(self, url, username, password):
        self.base_url = url
        self.username = username
        self.password = password

        self.page = atlassian_password.ClearPasswordOnException(username).decorator(self.page)
        self.save_content = atlassian_password.ClearPasswordOnException(username).decorator(self.save_content)

    def page(self, page_id):
        query = { 'expand': 'version'}
        url = self.base_url + '/rest/api/content/' + page_id + '?' + urllib.urlencode(query)
        response =  requests.get(url, auth=(self.username, self.password), headers={'Accept': 'application/json'})
        response.raise_for_status()
        retval = response.json()

        if 'errorMessages' in retval:
            raise ValueError(page_id + ': ' + ','.join(retval['errorMessages']))

        return retval

    def get_page_id(self, space, title):
        try:
            url = self.base_url + '/rest/api/content/?title=' + title + '&spaceKey=' + space
            response = requests.get(url, auth=(self.username, self.password), headers={'Accept': 'application/json'})
            response.raise_for_status()
            retval = response.json()

            if 'errorMessages' in retval:
                raise ValueError(title + ': ' + ','.join(retval['errorMessages']))

            return retval["results"][0]["id"]
        except:
            return None

    def new_child_page(self, parent_page_id, space, title, content):
        data = json.dumps({
            'type': 'page',
            'title': title,
            'ancestors': [{"id": parent_page_id}],
            'space': {"key": space},
            'body': {
                'storage': {
                    'value': content,
                    'representation': 'storage'
                }
            }
        })

        page_id = self.get_page_id(space, title)

        if page_id is not None:
            page = self.page(page_id)

            data = json.dumps({
                'id': page_id,
                'type': 'page',
                'title': title,
                'version': {'number': page['version']['number'] + 1},
                'space': {'key': space},
                'body': {
                    'storage': {
                        'value': content,
                        'representation': 'storage'
                    }
                }
            })
            url = self.base_url + '/rest/api/content/' + page_id
            response = requests.put(url, auth=(self.username, self.password), headers={'Accept': 'application/json', 'Content-type': 'application/json'}, data=data)
            response.raise_for_status()
            retval = response.json()

            if 'errorMessages' in retval:
                raise ValueError(page_id + ': ' + ','.join(retval['errorMessages']))

            return retval
        else:
            url = self.base_url + '/rest/api/content'
            response = requests.post(url, auth=(self.username, self.password), headers={'Accept': 'application/json', 'Content-type': 'application/json'}, data=data)
            response.raise_for_status()
            retval = response.json()

            if 'errorMessages' in retval:
                raise ValueError(page_id + ': ' + ','.join(retval['errorMessages']))

            return retval

    def save_content(self, page_id, version, title, content):
        data = json.dumps({
            'type': 'page',
            'title': title,
            'version': { 'number': version},
            'body': {
                'storage': {
                    'value': content,
                    'representation': 'storage'
                }
            }
        })
        url = self.base_url + '/rest/api/content/' + page_id
        response = requests.put(url, auth=(self.username, self.password), headers={'Accept': 'application/json', 'Content-type': 'application/json'}, data=data)
        response.raise_for_status()
        retval = response.json()

        if 'errorMessages' in retval:
            raise ValueError(page_id + ': ' + ','.join(retval['errorMessages']))

        return retval