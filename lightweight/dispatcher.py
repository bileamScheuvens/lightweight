import os
from importlib import import_module


# lookup of name to location and class name
DISPATCH_COMPONENTS = {
    "model": {
        "random": ["models", "RandomModel"]
    },
    "datamodule": {
        "default": ["data", "CustomDataModule"]
    },
    "callback": {
        "default": ["callbacks", "CustomCallback"]
    }
}
def dispatch_component(component, config, *args, **kwargs):
    assert component in DISPATCH_COMPONENTS.keys(), f"Invalid component type {component}"
    config = config[component]
    com_module, com_class = DISPATCH_COMPONENTS[component][config["name"]]
    # lazy import
    import_path = f"{os.path.basename(os.path.dirname(__file__))}.{com_module}" 
    component = getattr(import_module(import_path), com_class) 
    return component(*args, **config, **kwargs)
