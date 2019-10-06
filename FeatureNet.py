import torch.nn as nn
import torch.nn.functional as F

class FeatureNet(nn.Module):
    def __init__(self, feature_Size = 16*5*5):
        super(FeatureNet, self).__init__()
        self.fc1 = nn.Linear(feature_Size, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x