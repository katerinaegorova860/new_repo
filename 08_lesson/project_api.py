import requests


class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # Создание проекта
    def create_project(self, title, description=None, users=None):
        if users is None:
            users = {}
        data = {"title": title, "users": users}
        if description:
            data["description"] = description
        response = requests.post(f"{self.base_url}/projects", headers=self.headers, json=data)
        return response

    # Изменение проекта
    def update_project(self, project_id, title=None, description=None, users=None):
        data = {}
        if title:
            data["title"] = title
        if description:
            data["description"] = description
        if users:
            data["users"] = users
        response = requests.put(f"{self.base_url}/projects/{project_id}", headers=self.headers, json=data)
        return response

    # Получение проекта по ID
    def get_project(self, project_id):
        response = requests.get(f"{self.base_url}/projects/{project_id}", headers=self.headers)
        return response
