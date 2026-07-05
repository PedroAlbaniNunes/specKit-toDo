from app_package.main import app


def test_index_page_renders_template():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Task Manager MVC" in response.data
