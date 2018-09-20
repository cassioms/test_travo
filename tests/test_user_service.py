import os

from pytest import fixture

from aula03.user_service import UserService


@fixture
def user_service():
    yield UserService('test.db')
    if os.path.exists("test.db"):
        os.remove("test.db")
    else:
        print("test.db does not exist")


def test_add_user(user_service):
    user_service.add_user(1, 'mock', 1.70, 80.0)
    user_list = user_service.list_users()
    assert len(user_list) == 1
    assert user_list[0]['name'] == 'mock'


def test_delete_user(user_service):
    user_service.add_user(1, 'mock', 1.70, 80.0)
    user_service.delete_user(1)
    user_list = user_service.list_users()
    assert len(user_list) == 0


def test_update_user(user_service):
    user_service.add_user(1, 'mock', 1.70, 80.0)
    user_service.update_user(1, 'upmock', 1.50, 60.0)
    user_list = user_service.list_users()
    assert len(user_list) == 1
    assert user_list[0]['name'] == 'upmock'
    assert user_list[0]['height'] == 1.50
    assert user_list[0]['weight'] == 60.0


def test_list_users(user_service):
    user_service.add_user(1, 'mock', 1.70, 85.0)
    user_service.add_user(2, 'mock2', 1.90, 65.0)
    user_service.add_user(3, 'mock3', 1.65, 65.0)
    user_list = user_service.list_users()
    print(user_list)
    assert len(user_list) == 3
    assert user_list[0]['name'] == 'mock3'
    assert user_list[0]['level'] == 0
    assert user_list[1]['name'] == 'mock2'
    assert user_list[1]['level'] == 1
    assert user_list[2]['name'] == 'mock'
    assert user_list[2]['level'] == 2
