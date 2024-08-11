import pytest

from lightweight.dispatcher import dispatch_component

def test_model(config):
    model = dispatch_component("model", config)
    # TODO: test functionality