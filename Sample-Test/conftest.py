import pytest

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1",
        help="Enter the url for")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")