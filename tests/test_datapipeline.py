import pytest

from lightweight.dispatcher import dispatch_component, DISPATCH_COMPONENTS

@pytest.mark.parametrize("dataloader", DISPATCH_COMPONENTS["datamodules"].keys())
def test_dataloader(dataloader):
    dataloader = dispatch_component("dataloader", dataloader)
    # TODO: test functionality