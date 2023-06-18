import abc

from .iter_dataset import *
from abc import ABC


class BaseModel:
    def __init__(self, dataset: [IterDataset]):
        self.dataset = dataset

    @abc.abstractmethod
    def fit(self):
        pass
