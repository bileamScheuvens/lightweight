import pytest

from lightweight.dispatcher import dispatch_component

def test_datamodule(config):
    datamodule = dispatch_component("datamodule", config) 
    # TODO: test functionality