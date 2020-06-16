import requests
import random
import os

base_uri = os.getenv('API_HOST', http://localhost)
port = os.getenv('API_PORT',3000)
posts_uri = f'{base_uri}:{port}/posts'


def test_api_get_posts():
	r = request.get(posts_uri)
	assert r.status_code == 200

def test_creating_post():
	marker = random.randint(100000)
	body = {'title': 'test post', 'author': 'ag'}
	r = request.post(posts_uri, json=body)
	assert r.status_code == 200
