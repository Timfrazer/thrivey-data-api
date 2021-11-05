import pytest
from fastapi.testclient import TestClient
from multiprocessing import Process

from app.main import app, run_server


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start() 
    yield
    proc.kill() # Cleanup after test


# import pytest
# import responses

# from fastapi.testclient import TestClient
# from fastapi import FastAPI

# from httpx import AsyncClient
# import asyncio


# def make_app():
#     from app.main import app

#     # Config your app here
#     return app

# @pytest.fixture
# def test_fixture(loop, test_client):
#     """Test fixture to be used in test cases"""
#     app = make_app()
#     return loop.run_until_complete(test_client(app))

# # @pytest.fixture(scope="module")
# # def test_app():
# #     client = TestClient(app)
# #     yield client  # testing happens here


# # app = FastAPI()

# # # Fixtures
# # @pytest.fixture
# # def client():
# #     with TestClient(app) as tc:
# #         yield tc

# # @pytest.fixture
# # def loop(client):
# #     yield client.task.get_loop()


# # @pytest.fixture
# # def mocked_responses():
# #     with responses.RequestsMock() as resp:
# #         yield resp

# # @pytest.fixture
# # async def client(initialized_app: FastAPI) -> AsyncClient:
# #     async with AsyncClient(
# #         app=initialized_app,
# #         base_url="http://testserver",
# #         headers={"Content-Type": "application/json"},
# #     ) as client:
# #         yield client


# # @pytest.fixture
# # def db_fixture() -> Session:
# #     raise NotImplementError()  # Make this return your temporary session

# # @pytest.fixture
# # def client(db_fixture) -> TestClient:

# #     def _get_db_override():
# #         return db_fixture

# #     app.dependency_overrides[get_db] = _get_db_override
# #     return TestClient(app)
