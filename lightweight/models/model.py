import pytorch_lightning as pl
import torch

class RandomModel(pl.LightningModule):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.total_bias = torch.nn.Parameter(torch.tensor(0.0))

    def forward(self, x):
        return torch.rand(x.shape[0]) + self.total_bias

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters())
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = torch.nn.functional.mse_loss(y_hat, y)
        return loss