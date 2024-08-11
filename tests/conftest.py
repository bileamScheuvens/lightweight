import pytest
import os
import yaml

@pytest.fixture(scope="session")
def config():
    with open(f"{os.path.dirname(__file__)}/../configs/test.yaml") as f:
        config = yaml.safe_load(f)
    return config["parameters"]