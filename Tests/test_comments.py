import pytest 
import requests
import json
movies_url = "http://127.0.0.1:8000/api"

def test_get_comments():
    url = movies_url + "/comments"
    resp = requests.get(url)
    assert resp.status_code == 200


def test_post_comments():
    movie = 11
    url = movies_url + "/comments/"
    data = {
        "movie": movie,
        "text": "This movie is good"
    }
    resp = requests.post(url, data)
    assert resp.status_code == 201