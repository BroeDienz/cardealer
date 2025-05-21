from locust import HttpUser, TaskSet, task, between

class CarApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_cars(self):
        self.client.get("/api/cars")
