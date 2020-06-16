import random
from locust import HttpUser, task, between

class QueryAPI(HttpUser):
	wait_time = between(1, 2)

	@task
	def get_posts(self):
		self.client.get("/posts")

	@task
	def get_comments(self):
		self.client.get("/comments")
