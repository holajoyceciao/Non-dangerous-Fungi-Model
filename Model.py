import torch
import torchvision
from torchvision import transforms
import torch.nn as nn

class MyClassifier():
    
    def __init__(self):
        self.class_labels = ['edible_1', 'edible_2', 'edible_3', 'edible_4', 'edible_5', 'poisonous_1', 'poisonous_2', 'poisonous_3', 'poisonous_4', 'poisonous_5'] 
        
    def setup(self):
        ''' 
        Load the model architecture and load any saved weights file the model relies on.
        '''

        # init model
        self.model = torchvision.models.resnet18()
        self.model.fc = nn.Sequential(nn.Dropout(p=0.3, inplace=True),
                             nn.Linear(self.model.fc.in_features, len(self.class_labels))
                            )
        self.model.load_state_dict(torch.load('resnet18.pth', map_location='cpu'))
        self.model.eval()

        # image transform
        pre_weights = torchvision.models.ResNet18_Weights.DEFAULT
        transform = pre_weights.transforms()
        self.transform = transforms.Compose([
                                              transform
                                            ])

        print(f'[INFO] Preprocessing steps successfully defined.')
        
    def test_image(self, image):
        ''' 
        Return the predicted class label for that image. 
        '''
        
        img = self.transform(image).unsqueeze(0).to('cpu')
        with torch.no_grad():
            prediction = self.model(img)
        predicted_idx = torch.argmax(prediction, dim=1)
        predicted_cls = self.class_labels[predicted_idx.item()]
        
        return predicted_cls