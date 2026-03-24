#deep learning - 
#unstructured data - images, text, audio
#structured data - tabular data, time series
#deep learning is a subset of machine learning that uses neural networks with 
# many layers to learn from large amounts of data
#deep learning is used for image recognition, natural language processing, 
# speech recognition, and more
#deep learning is a powerful tool for solving complex problems, 
# but it requires a lot of data and computational power
#deep learning is a field of machine learning that uses neural networks 
# with many layers to learn from large amounts of data
#neural networks - a set of algorithms that are designed to recognize patterns
#neural networks are inspired by the structure and function of the human brain
#neural networks are used for image recognition, natural language processing,
#  speech recognition, and more


#keras - high level API for building and training deep learning models
#tensorflow - low level API for building and training deep learning models
#what is the difference between keras and tensorflow?
#keras is a high-level API that is built on top of tensorflow, making it easier to
#build and train deep learning models.
#  TensorFlow is a low-level API that provides more flexibility and 
# control over the model architecture and training process.


#in deep learning parameters are more and more finetuning is requered to build a good model

#ANN - Artificial Neural Network - A type of neural network that consists of an input layer,
#  one or more hidden layers, and an output layer. Each layer is made up of nodes 
# (neurons) that are connected to the nodes in the previous and next layers.
#DNN - Deep Neural Network - A type of neural network that has multiple hidden layers.
#  DNNs are capable of learning complex patterns in data and are used for tasks 
# such as image recognition, natural language processing, and speech recognition.
#CNN - Convolutional Neural Network (no memory )- A type of neural network that is 
# specifically designed for processing grid-like data, such as images.
#  CNNs use convolutional layers to automatically learn spatial hierarchies
#  of features from the input data, making them highly effective for image-related tasks.
#RNN - Recurrent Neural Network (memory - because we need to store the previous 
# data for prediction)- A type of neural network that is designed to work with 
# sequential data, such as time series or natural language. RNNs have loops in 
# their architecture that allow them to maintain a memory of previous inputs,
#  making them suitable for tasks like language modeling and speech recognition.

#deep learning is heavy weight model, and there are lot of parameter to fine tune
#transfer learning - already a pretrained model is available, llama, gpt, bert, etc. - 
# we can use these models to build our own model
#llama - Large Language Model Meta AI - a family of large language models developed 
# by Meta AI
#gemini - a family of large language models developed by Google DeepMind
#keras have pretrained models for image classification, object detection, and more.
#  eg - albumentation, mobilenet, resnet, vgg, etc.
#we use the pretrained models to build our own model by adding our own layers 
# on top of the pretrained model
#example of transfer learning - using a pretrained model like VGG16 or ResNet50
#  for image classification tasks, where we can add our own layers on top of the 
# pretrained model to classify images into specific categories.


#objet detection - a computer vision task that involves identifying and locating objects in
#  images or videos
#it is used to segment images into different regions based on the objects present in the
#  image
#it is used in self driving cars, robotics, and more
#yolo - You Only Look Once - a popular object detection algorithm that uses a single
#  neural network to predict bounding boxes and class probabilities for multiple objects
#  in an image
#yolo is a real time object detection algorithm that is fast and accurate
#yolo is used for object detection in images and videos, and it is used in self driving 
# cars, robotics, and more

#RNN - Recurrent Neural Network - A type of neural network that is designed to work with
#  sequential data, such as time series or natural language. RNNs have loops in their 
# architecture that allow them to maintain a memory of previous inputs,
#  making them suitable for tasks like language modeling and speech recognition.
#used for text generation, language translation, and more
#NLP - Natural Language Processing - A field of AI that focuses on the interaction
#  between computers and humans through natural language. NLP is used for tasks 
# such as text classification, sentiment analysis, language translation, and more.
#what is GPT- Generative Pre-trained Transformer - A type of large language model
#  that uses a transformer architecture to generate human-like text.
#  GPT models are pre-trained on large datasets and can be fine-tuned for specific tasks
#  such as text generation, language translation, and more.

#autoencoders - A type of neural network that is used for unsupervised learning.
#  Autoencoders learn to compress and reconstruct data by encoding it into a 
# lower-dimensional representation and then decoding it back to the original input.
#  They are used for tasks such as dimensionality reduction, anomaly detection,
#  and image denoising.
#used for speech transcription, image denoising, and more
#it will encode the input data into - latent variable - a lower-dimensional 
# representation of the input data
#and then decode it back to the original input  
#also called a sequence to sequence model

#keras is beter then pytorch for beginners because it is easier to use and has a lot 
# of prebuilt models and layers
#pytorch is more flexible and powerful, but it requires more knowledge of deep learning 
# concepts and it is more difficult to use for beginners


#MCP - 
#langraph - 
#microsoft deep learning models - 

#pretrained models
#imagenet challenge - classification task - a large-scale image classification competition
#  that has been held annually since 2010. It is one of the most prestigious competitions
#  in the field of computer vision and deep learning. The goal of the competition is
#  to classify images into one of 1000 categories, and it has led to significant 
# advancements in deep learning and computer vision techniques.
#the imagenet dataset is a large-scale dataset of images that is used for training 
# and evaluating deep learning models for image classification tasks.
#  It contains over 14 million images labeled with more than 20,000 categories,
#  making it one of the largest and most diverse image datasets available.
#the imagenet challenge has led to the development of many state-of-the-art deep
#  learning models, such as AlexNet, VGG, ResNet, and Inception. These models have
#  achieved remarkable performance on image classification tasks and have been widely 
# adopted in the field of computer vision.
#the imagenet dataset is used to train and evaluate deep learning models for image 
# classification tasks. It is a large-scale dataset that contains over 14 million images
#  labeled with more than 20,000 categories.

#deep learning eleiminates the manual feature engineering process, allowing models to 
# automatically learn relevant features from raw data. This is particularly useful 
# for unstructured data such as images, text, and audio, where traditional feature
#  extraction methods may not be effective.
#deep learning models are typically trained using large datasets and require significant 
# computational resources, such as GPUs or TPUs, to achieve good performance. 
# This is because deep learning models have many parameters that need to be optimized
#  during training, and the training process can be computationally intensive.
#deep learning models can be used for a wide range of tasks, including image 
# classification, object detection, natural language processing, speech recognition,
#  and more. They have achieved state-of-the-art performance in many of these tasks 
# and are widely used in industry and research.

#what is the difference between GPU and CPU?
#GPU (Graphics Processing Unit) is a specialized hardware designed for parallel processing,
#  making it ideal for tasks that require high computational power,
#  such as deep learning and image processing. It can handle thousands of threads 
# simultaneously, allowing for faster training of deep learning models compared
#  to a CPU (Central Processing Unit), which is designed for general-purpose computing
#  and typically has fewer cores optimized for sequential tasks.
#GPU is used for training deep learning models because it can handle
#  large amounts of data and perform complex calculations in parallel, 
# making it much faster than a CPU for tasks like matrix multiplication
#  and convolution operations.
#CPU is used for tasks that require sequential processing,
#  such as data preprocessing, model evaluation, and inference. 
# It is also used for tasks that do not require high computational power,
#  such as running simple algorithms or handling small datasets.

#text embeddings - a technique used to represent words or phrases as vectors in a 
# continuous vector space. This allows for capturing semantic relationships between
#  words and is commonly used in natural language processing tasks such as text 
# classification, sentiment analysis, and language translation.
#bag of words - a simple text representation technique that represents a document
#  as a collection of words, disregarding the order and grammar. It is often used 
# as a baseline for text classification tasks, but it does not capture semantic 
# relationships between words.
#word2vec (word to vector)- a popular algorithm for generating word embeddings that 
# uses a shallow neural network to learn word representations based on their context
#  in a large corpus of text. It can be trained using either the Continuous Bag of Words 
# (CBOW) or Skip-Gram model.
#GloVe (Global Vectors for Word Representation) - another popular algorithm for generating
#  word embeddings that uses matrix factorization techniques to learn word representations
#  based on their co-occurrence statistics in a large corpus of text. 
# It captures global statistical information about word co-occurrences, making it 
# effective for capturing semantic relationships between words.

#GAN- Generative Adversarial Network - A type of neural network architecture that consists
#  of two networks: a generator and a discriminator. The generator creates synthetic data,
#  while the discriminator evaluates the authenticity of the generated data.
#  GANs are used for tasks such as image generation, video synthesis, and data 
# augmentation.
#GANs are trained in an adversarial manner, where the generator tries to produce 
# realistic data
#generator - creates synthetic data
#discriminator - evaluates the authenticity of the generated data
#GANs are used for tasks such as image generation, video synthesis, 
# and data augmentation. They have been used to create realistic images, videos, and
#  even music.
#example - generator will generate 10 images and pass to disciminator and it will 
# evalute if the image maches with real image. If difference is found then 
#  the generator will create more images and the same prcess will follow,
#  till the simalar image is created

#the generator and discriminator are trained together in a process called adversarial 
# training, where the generator tries to fool the discriminator into thinking that the
#  generated data is real, while the discriminator tries to correctly classify the data
#  as real or fake.
#this adversarial training process leads to the generator producing increasingly realistic
#  data over time, while the

#Once the collected data gets labeled, the project then moves to the training phase.
# During Deep Learning training, the model learns from data by iteratively adjusting
#  its parameters through forward and backward propagation. This minimizes errors
#  and enhances predictions.