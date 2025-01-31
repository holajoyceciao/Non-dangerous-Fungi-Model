# Non-dangerous-Fungi-Model
This app is trained with 1,001 images with 10 classes of fungi using fine-tuning Resnet18. 

#### Source 
- [Data]()
- [Non-dangerous-Fungi - Source Code]()
- PyTorch - [RestNet18](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet18.html#torchvision.models.ResNet18_Weights)

# Model Goal:
The model should be able to identify edible and poisonous fungi species (binary classification, behind the scenes is 10-classes classification)
#### Model Purpose
- Improve the fungi education to the public
- Encourage to remove poisonous fungi species
- Encourage to appreciate non-dangerous fungi species

# Experiment with different Optimizer
- Adam has better performance in both accuracy and loss parts (The parameters are the same)
- Due to the learning rate having a major impact on the accuracy and overfitting, Adam can adjust the learning rate by itself while SGD needs to be adjusted manually.
#### Default Parameter
  ![image](https://github.com/user-attachments/assets/03905749-ba13-4bb8-8874-e33acfa64905)

#### Hyperparameters
   ![image](https://github.com/user-attachments/assets/1bfb9a48-e390-4c5b-8043-7d8f383059bb)

#### Results
   ![image](https://github.com/user-attachments/assets/fec18c9f-aa70-4aaf-91c7-7398338b337a)

# Overview
- Fine-tuned Pre-trained weight Resnet18 with adding Adam optimizer to decrease overfitting and data augmentation (TrivialAugmentWide) to increase the variety of images.
- 74% Accuracy is sufficient for educational use given the amount of data available.
- The trade-off of 83% precision and 85% recall is relatively balanced. This shows the model can correctly identify poisonous fungi and minimize the misclassifications of edible species.

  ![image](https://github.com/user-attachments/assets/b568c643-0c81-47c1-87fb-3ca196d1a3bc)
  
# Model Limitation
- Imbalanced Data Classification may affect the model's ability to generalize well on all classes.
- The model may not have enough data to learn the features of all classes, which may prevent it from reaching its full potential.
- Fungi species outside of Brisbane might be miscategorized in one of the classes

# Recommendation for how this model should be used
- Do not 100% rely on predictions, especially for potentially dangerous fungi species.
- Provide additional function for users to provide additional information (e.g. how many percentages confident is model predicting this as edible or poisonous)


