"""Machine learning pipelines supporting encrypted data."""

from typing import Tuple

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


class LSTMModel(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 64):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 2)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])


def train_lstm(data: np.ndarray, labels: np.ndarray) -> LSTMModel:
    model = LSTMModel(data.shape[2])
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    tensor_x = torch.tensor(data, dtype=torch.float32)
    tensor_y = torch.tensor(labels, dtype=torch.long)
    for _ in range(5):
        optimizer.zero_grad()
        outputs = model(tensor_x)
        loss = criterion(outputs, tensor_y)
        loss.backward()
        optimizer.step()
    return model


def train_resnet(data: np.ndarray, labels: np.ndarray) -> Tuple[nn.Module, float]:
    model = torch.hub.load("pytorch/vision", "resnet18", pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 2)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    tensor_x = torch.tensor(data, dtype=torch.float32)
    tensor_y = torch.tensor(labels, dtype=torch.long)
    for _ in range(2):
        optimizer.zero_grad()
        outputs = model(tensor_x)
        loss = criterion(outputs, tensor_y)
        loss.backward()
        optimizer.step()
    preds = model(tensor_x).argmax(dim=1).numpy()
    acc = accuracy_score(labels, preds)
    return model, acc


def train_xgboost(data: np.ndarray, labels: np.ndarray) -> XGBClassifier:
    clf = XGBClassifier(n_estimators=50, max_depth=3, verbosity=0)
    clf.fit(data, labels)
    return clf
