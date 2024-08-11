import pytorch_lightning as pl

class CustomCallback(pl.Callback):
    def __init__(self, wandb_run=None, *args, **kwargs) -> None:
        super().__init__()
        self.run = wandb_run
        self._empty_cache = {
            "some_metric": 0,
        }
        self.train_cache = self._empty_cache.copy()
        self.val_cache = self._empty_cache.copy()


    def on_train_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        self.run.log({"train_loss": outputs["loss"]})
        if "some_metric" in outputs:
            self.train_cache["some_metric"] += outputs["some_metric"]

    def on_train_epoch_end(self, trainer, pl_module):
        self.run.log({"train_some_metric": self.train_cache["some_metric"]})
        self.train_cache = self._empty_cache.copy()

    def on_validation_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        self.run.log({"val_loss": outputs["loss"]})
        if "some_metric" in outputs:
            self.val_cache["some_metric"] += outputs["some_metric"]

    def on_validation_epoch_end(self, trainer, pl_module):
        self.run.log({"val_some_metric": self.val_cache["some_metric"]})
        self.val_cache = self._empty_cache.copy()