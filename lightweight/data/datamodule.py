"""Dataloader"""

import torch
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl
from sklearn.model_selection import train_test_split


class CustomDataset(Dataset):

    def __init__(self, X, y, config):
        super().__init__()
        self.config = config
        self.X = torch.tensor(X).float()
        self.y = torch.tensor(y).float()

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

class CustomDataModule(pl.LightningDataModule):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.batch_size = config["batch_size"]
        self.val_split = config["val_split"]
        self.test_split = config["test_split"]

    def prepare_data(self):
        # This method is used to do things that might write to disk or need to be done only from a single GPU, like downloading data.
        self.data = torch.randn(1000, 10)
        self.labels = torch.rand(1000) > 0.5

    def setup(self, stage=None):
        # Split the data into train, validation, and test sets
        data_train, data_tmp, labels_train, labels_tmp = train_test_split(self.data, self.labels, test_size=self.val_split + self.test_split)
        data_val, data_test, labels_val, labels_test = train_test_split(data_tmp, labels_tmp, test_size=self.test_split / (self.val_split + self.test_split))

        self.train_dataset = CustomDataset(data_train, labels_train, config=self.config["dataset"])
        self.val_dataset = CustomDataset(data_val, labels_val, config=self.config["dataset"])
        self.test_dataset = CustomDataset(data_test, labels_test, config=self.config["dataset"])

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size)
