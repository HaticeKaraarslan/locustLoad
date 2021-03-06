from locust import  HttpLocust, TaskSet

def get_homepage(l):
    response= l.client.get("/")
    print(response.status-code)
    print(response.content)

def get_electronic_tab(l):
    l.client.get("elektronik")

class UserBehavior(TaskSet) :
    tasks = {get_homepage: 2, get_electronic_tab: 1}

class WebsiteUser(HttpLocust) :
    task_set = UserBehavior
    min_wait = 900
    max_wait = 5000
    host = "https://www.n11.com"