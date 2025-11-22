import pytest
from project_api import ProjectAPI

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "VzfkPTkCmbuLPBGqtUj7dcbUZMMOiKB-LTnKSe2mD91ye9YiX4WQv0VPeohh5oU5"
USER_ID = "50c0414b-4e71-430d-ab30-92951df15006"

api = ProjectAPI(BASE_URL, TOKEN)


@pytest.fixture
def created_project():
    users = {USER_ID: "worker"}
    resp = api.create_project("Autotest Project", users=users)
    assert resp.status_code in [200, 201]
    project = resp.json()
    yield project

# Создание проекта

# Позитив

def test_create_project_positive():
    users = {USER_ID: "worker"}
    resp = api.create_project("Positive Project", users=users)
    assert resp.status_code in [200, 201]
    body = resp.json()
    assert "id" in body  # проверяем, что вернулся id


# Негатив
def test_create_project_negative_missing_title():
    users = {USER_ID: "worker"}
    resp = api.create_project("", users=users)
    assert resp.status_code == 400

# Изменение проекта

# Позитив

def test_update_project_positive(created_project):
    project_id = created_project["id"]
    users = {USER_ID: "worker"}
    resp = api.update_project(project_id, title="Updated Project", users=users)
    assert resp.status_code in [200, 201]
    body = resp.json()
    assert "id" in body


# Негатив
def test_update_project_negative_invalid_id():
    resp = api.update_project("00000000-0000-0000-0000-000000000000", title="Fail")
    assert resp.status_code == 404

# Получение проекта по ID
# Позитив

def test_get_project_positive(created_project):
    project_id = created_project["id"]
    resp = api.get_project(project_id)
    assert resp.status_code in [200, 201]
    body = resp.json()
    assert body["id"] == project_id


# Негатив
def test_get_project_negative_invalid_id():
    resp = api.get_project("00000000-0000-0000-0000-000000000000")
    assert resp.status_code == 404
