import os
import json
import urllib.request
import urllib.parse

def canvas_full_url(url):
    if url[:4] != 'http':
        url = "https://canvas.instructure.com/api/v1/" + url

    return url

def canvas_get(url, data=None, auth=True):
    url = canvas_full_url(url)

    print(f"URL: {url}")

    if auth:
        if data is None:
            data = {}

        data["access_token"] = os.environ["CANVAS_API_ACCESS_TOKEN"]
        data["per_page"] = "200"

    return get(url, data)

def canvas_post(url, data=None, auth=True):
    return canvas_post_put(url, data, auth, method="POST")

def canvas_put(url, data=None, auth=True):
    return canvas_post_put(url, data, auth, method="PUT")

def canvas_post_put(url, data=None, auth=True, method="POST"):
    url = canvas_full_url(url)

    print(f"URL: {url}")

    if auth:
        if data is None:
            data = {}

        data["access_token"] = os.environ["CANVAS_API_ACCESS_TOKEN"]

    headers = {
        "Authorization": f'Bearer {os.environ["CANVAS_API_ACCESS_TOKEN"]}'
    }

    return post_put(url, data, headers, "POST")

def get(url, data=None):
    if data is not None:
        url += '?' + urllib.parse.urlencode(data)

    req = urllib.request.Request(url, method='GET')

    resp = urllib.request.urlopen(req)

    data = resp.read()

    return data, resp.getheaders()

def post_put(url, data=None, headers=None, method="POST"):
    if data is not None:
        #data = urllib.parse.urlencode(data).encode()
        data = json.dumps(data).encode()

    headers['Content-Type'] = "application/json"
    print(data)
    print(headers)

    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    resp = urllib.request.urlopen(req)

    data = resp.read()

    return data, resp.getheaders()
