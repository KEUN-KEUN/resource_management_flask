import pytest
from unittest.mock import patch, MagicMock
from allocation.entrypoints import flask_app  # flask_app.py 모듈 import


@pytest.fixture
def client():
    """Flask 테스트 클라이언트 생성"""
    app = flask_app.app
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


# sql 쿼리 결과 확인 테스트
def test_health_actual_sql(client):
    """실제 DB 쿼리 결과를 확인하는 통합 테스트"""
    response = client.get("/api/health")
    json_data = response.get_json()

    # 검증
    assert response.status_code == 200
    assert "status" in json_data
    assert "user" in json_data

    # DB에 ADMIN이 실제 존재한다면, USER_NAME 필드 확인
    if json_data["user"]:
        print(f"USER_NAME: {json_data['user'].get('USER_NAME')}")
        assert json_data["user"].get("USER_NAME") is not None