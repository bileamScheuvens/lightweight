import pytest

from lightweight.dispatcher import dispatch_component, DISPATCH_COMPONENTS

@pytest.mark.parametrize("model", DISPATCH_COMPONENTS["models"].keys())
def test_model(model):
    model = dispatch_component("model", model)
    # TODO: test functionality