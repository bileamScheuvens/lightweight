import pytest
import yaml

@pytest.fixture(scope="session")
def config():
    with open("../configs/test.yaml") as f:
        config = yaml.safe_load(f)
    return config