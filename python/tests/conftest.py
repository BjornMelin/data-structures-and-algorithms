import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_dict():
    return {"a": 1, "b": 2, "c": 3}

@pytest.fixture
def sample_set():
    return {1, 2, 3, 4, 5}

@pytest.fixture
def sample_tuple():
    return (1, 2, 3, 4, 5)

@pytest.fixture
def sample_string():
    return "hello world"

@pytest.fixture
def sample_int():
    return 42

@pytest.fixture
def sample_float():
    return 3.14

@pytest.fixture
def sample_bool():
    return True

@pytest.fixture
def sample_none():
    return None

@pytest.fixture
def sample_complex():
    return 1 + 2j
