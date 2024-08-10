from lightweight.models.model import RandomModel
from lightweight.callbacks.callback import CustomCallback
from lightweight.data.datamodule import CustomDataModule



DISPATCH_COMPONENTS = {
    "models": {
        "random": RandomModel
    },
    "datamodules": {
        "default": CustomDataModule
    },
    "callbacks": {
        "default": CustomCallback
    }
}
def dispatch_component(component, config, *args, **kwargs):
    assert component in DISPATCH_COMPONENTS.keys(), f"Invalid component type {component}"
    return DISPATCH_COMPONENTS[component][config[component]["name"]](**config[component], *args, **kwargs)