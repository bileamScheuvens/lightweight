import torch
from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.callbacks import ModelCheckpoint
from lightweight.dispatcher import dispatch_component
import wandb
import yaml

seed_everything(1)
torch.set_float32_matmul_precision("medium")

def run_config(config=None):
    with wandb.init(config=config) as run:
        config = wandb.config
        datamodule = dispatch_component("datamodule", config)
        datamodule.prepare_data()
        datamodule.setup("fit")
        model = dispatch_component("model", config)
        trainer = Trainer(
            logger=[],
            callbacks=[dispatch_component("callback", config, run=run)],
            enable_checkpointing=False,
            **config["trainer"]
        )
        trainer.fit(model, datamodule=datamodule)


def sweep(config_path="configs/sweep.yaml"):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    sweep_id = wandb.sweep(config, project="sweepsink")
    wandb.agent(sweep_id, function=run_config, count=30)

def train(config_path="configs/train.yaml", offline=False):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    callbacks=[ModelCheckpoint(dirpath="../checkpoints")]
    if not offline:
        run = wandb.init(project="lightweight", name=config["name"])
        callbacks.append(dispatch_component("callback", config, run=run))
    
    config = config["parameters"]
    datamodule = dispatch_component("datamdoule", config)

    trainer = Trainer(
        logger=[],
        callbacks=callbacks,
        **config["trainer"]
    )
    model = dispatch_component("model", config)
    trainer.fit(model, datamodule=datamodule)
    

def train_offline(config_path="configs/train.yaml"):
    train(config_path, offline=True)
    
    