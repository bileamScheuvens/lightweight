## Template for the LightWeight (pytorch lighting + W&B) Stack


#### Usage
- fork
- rename (incl. pyproject.toml)
- ```poetry install```
- implement:
    - Dataloader
    - Model
    - Callbacks
- add components to dispatcher.py
- adjust configs as needed
- ```wandb login```
- ```poetry run <train|train_offline|sweep>```


#### Directory Structure
```
├── checkpoints/
│   └── *.ckpt
├── configs/
│   └── *.yaml
├── data/
│   └── ...
├── tests/
│   ├── conftest.py
│   └── ...
└── lightweight/
    ├── callbacks/
    │   └── ...
    ├── data/
    │   └── datamodule.py
    ├── models/
    │   └── *.py
    ├── __init__.py
    └── dispater.py // maintains known models etc.
```


#### TODO:
- tests
- setup script (cookiecutter?)
