## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        #Image Input_size=224x224 (as suggested), grayscale
        #input: 1(grayscale),32(feature_maps),5(5x5 filter)
        self.conv1=nn.Conv2d(1,32,5)
        #output: 32, (224-5)/1 + 1= 220,
        self.pool1 = nn.MaxPool2d(2, 2)
        #output: 32, 220/2= 110,
        self.do1=nn.Dropout(0.2)
        #input: 32,64(feature_maps),5(5x5 filter)
        self.conv2=nn.Conv2d(32,64,5)
        #output: 64, (60-5)/1+1=106
        self.pool2 = nn.MaxPool2d(2, 2)
        #output: 64, 53, 53
        self.do2=nn.Dropout(0.2)
        self.fc1=nn.Linear(64*53*53,500)
        self.fc2=nn.Linear(500,136)
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        #self.conv1 = nn.Conv2d(1, 32, 5)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting)       
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        
        x= self.pool1(self.do1(F.relu(self.conv1(x))))
        x= self.pool2(self.do2(F.relu(self.conv2(x))))
        
        x=x.view(x.size(0),-1)
        x=F.relu(self.fc1(x))
        x=self.fc2(x)
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
    
#weight = torch.from_numpy(filters).unsqueeze(1).type(torch.FloatTensor)
#model = Net(weight)
#print(model)
