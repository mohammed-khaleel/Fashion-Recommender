import pickle
import numpy as np 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from tensorflow .keras.layers import GlobalMaxPooling2D


feature_list=np.array(pickle.load(open('embeddings.pkl','rb')))

