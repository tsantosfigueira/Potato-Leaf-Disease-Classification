# Potato-Leaf-Disease-Classification
Potato Leaf Disease Classification with Computer Vision

This a classification problem where the goal is to identify potato leaves as either healthy, late blight or early blight. It uses CNNs with Tensorflow;

This is inspired by the excellent base-model project available at: https://ashokpalivela.medium.com/potato-disease-classifier-end-to-end-deep-learning-project-960bc784aa47

Dataset: https://www.kaggle.com/datasets/ashokkumarpalivela/potato-diseases

Classes:
- Late Blight: Late blight of potato is a disease caused by fungus Phytophthora infestans.
- Early Blight: Early blight of potato is a disease caused by the fungus Alternaria solani
- Healthy: Uninfected or healthy plant

Example of potato leaves:

![image](https://github.com/user-attachments/assets/e14c367d-71ae-41fb-9706-01e19abf4fbf)


This model outperforms the base model:

| Model         | F1-Score (Weighted Avg) | F1-Score (Macro Avg) |
|---------------|-------------------------|----------------------|
| Base Model    | 0.97                    | 0.95                 |
| Improved Model| 0.98                    | 0.97                 |

with no sign of overfitting thanks to Early Stopping:

![image](https://github.com/user-attachments/assets/82073dea-2a28-4d78-a21d-be6f1b11f370)

You can verify the results in the /Model/ directory where the Jupyter Notebook is. I also built an API with FastAPI, to predict a class given an image.


