import pytest

from lightweight.dispatcher import dispatch_component, DISPATCH_COMPONENTS

@pytest.mark.parametrize("callback", DISPATCH_COMPONENTS["callbacks"].keys())
def test_callback(callback):
    callback = dispatch_component("callback", callback)
    # TODO: test functionality