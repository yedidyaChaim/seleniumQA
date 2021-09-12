import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/stage.supplant.me")
        self.client.get("/stage.supplant.me/home/dashboard")

    @task
    def hello_world(self):
        self.client.get("https://stage.supplant.me:443/webfront-0.0.1/api/v2/grower/126/plot/3441/measurement/PREVIEW")

    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"yedidya@supplant.me", "password":"1q2w3e4r"})