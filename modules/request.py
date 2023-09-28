import os
import urllib.request
import urllib.parse

def canvas_get(url, data=None, auth=True):
    if url[:4] != 'http':
        url = "https://canvas.instructure.com/api/v1/" + url

    if auth:
        if data is None:
            data = {}

        data["access_token"] = os.environ["CANVAS_API_ACCESS_TOKEN"]
        data["per_page"] = "200"

    return get(url, data)

def get(url, data=None):
    if data is not None:
        url += '?' + urllib.parse.urlencode(data)

    req = urllib.request.Request(url, method='GET')

    resp = urllib.request.urlopen(req)

    data = resp.read()

    return data, resp.getheaders()



