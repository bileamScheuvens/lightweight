## Template for the LightWeight (pytorch lighting + W&B) Stack


#### Usage
- clone
- rename (incl. pyproject.toml)
- ```poetry install```
- implement:
    - Dataloader
    - Model
    - Callbacks
- adjust configs as needed
- ```wandb login```
- ```poetry run <train|train_offline|sweep>```
