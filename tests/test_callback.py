import pytest

from lightweight.dispatcher import dispatch_component, DISPATCH_COMPONENTS

def test_callback(config):
    callback = dispatch_component("callback", config, run=None)
    # TODO: test functionality