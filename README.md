# 🧠 Applied Machine Learning Tutorials
This repository contains Scikit-learn, PyTorch &amp; Keras tutorials and other teaching material for the CMP3006 course on Pattern Recognition at Cairo University.

The course covers the following topics, with lectures focusing on theoretical foundations and tutorials dedicated to demonstrating and analyzing concepts from the lecture:

![Algos-modified](https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/d930f765-4a4d-4aff-9170-23c365786ee9)


## 📅 Modus Operandi
Tutorials are held weekly on-campus, with each session lasting three contact hours with a total of about 14 tutorials per semester. They are designed to bridge the theoretical knowledge from the lecture to practice and provide real hands-on experience to students.

**Tutorials involve the following types of activities:**

<table >
  <tr>
    <th>Activity</th>
    <th>Methodology </th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>Weekly Quiz</td>
    <td>Solved collectively and in return of incentives such as chocolate or stickers</td>
    <td>Encourage and motivate students to review the previous tutorial and lecture content before coming to the tutorial</td>
  </tr>
  <tr>
    <td> Sheets</td>
    <td> Solved by TAs on the board during the tutorial session</td>
    <td> Deepen and solidify student understanding of different concepts covered in the lecture by working out written examples</td>
  </tr>
  <tr>
    <td> Labs </td>
    <td> Solved by students then evaluated by TAs through a discussion</td>
    <td> Ensure students can implement and analyze different machine learning techniques/models from scratch</td>
  </tr>
  <tr>
    <td> Demo Tutorials </td>
    <td> TA demonstrates and analyzes algorithms that are not covered in the labs </td>
    <td> For better comprehensiveness of theoretical content covered in the lectures</td>
  </tr>
  <tr>
    <td> Engineering Tutorials </td>
    <td> TA covers different ML engineering concepts while learning about relevant software toolboxes (e.g., PyThon, Scikit-Learn, Skikit-Image, PyTorch) </td>
    <td> Prepare students for workflow they will encounter in the industry and familiarize them with the different toolboxes available</td>
  </tr>
    <tr>
    <td> Engineering Project </td>
    <td> Students team up to implement machine learning cycles to solve an industry-like problem. This takes place as a competition  </td>
    <td> Simulate industry workflows and projects in the university</td>
  </tr>
  <tr>
    <td> Extras </td>
    <td> Optional material including to an introduction to Julia, an introduction to how LLMs work and case studies elaborating the machine learning industry in Egypt  </td>
    <td> Familiarize students with ML topics that are either trending or of high potential and make them aware of the hiring processes, nature of work and interview questions in the ML industry</td>
  </tr>
</table>


> [!IMPORTANT]  
> In this repository we only make material related to `Extras`, `Engineering Tutorials` and `Demo Tutorials` available. Upcoming TAs will have access to the full material; otherwise, please do not reuse this material for any purposes other than learning without seeking permission.

<details closed>
<summary>
  <h2> 👨🏻‍💻 Python Tutorials </h2>
</summary>
<br>
  
✦ In this series of tutorials we cover with students a comprehensive introduction to Python which makes use of their existing knowledge of C++ and covers:
  - PyThon basics, Types and Operators
  - Control Flow, Functions, OOP, Exceptions and Files
  - Essential packages such as Numpy, Pandas and Matplotlib

✦ By virtue of being comprensive, these also include advanced or sophisticated topics such as: 
- Type hints
- Decorators
- Generators
- Multithreading
- Calling C functions (high-level)
- Einsum
- Etc.

See the `Python Tutorials` folder to check out the tutorials.

  <div align="center" >
  <img src="https://www.newus.in/static/media/Core-python-at-newus-Dharmsala.0fc3b7c72cdea81baba4.gif" width="250"/>
</div>

</details>

<details closed>
<summary>
  <h2> 🍊 Scikit-learn Tutorials </h2>
</summary>
<br>
  
✦ In this series of tutorials we cover with students a comprehensive overview of the most widely used package in classical machine learning: Scikit-learn. Different major submodules are explored in the tutorials as shown:


<img width="1025" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/2966feea-80ef-4b00-b0e0-ab8dd17a3af7">

All modules shown are covered except those in grey. In this, students learn how to implement various elements in the machine learning cycle:

<img width="1197" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/9fff8cfe-c81d-4cd0-a5d3-824afcb1c0d1">

✦ This includes many basic and *advanced* machine learning engineering concepts including:

- Supervised, Semi-supervised and Unsupervised Learning
- Loading data, generating data as well as normalization and encoding methods
- Key machine learning metrics and different techniques for cross validation
- Learning curves, validation curves and different hyperparameter tuning techniques as well as logging
- Feature extraction, selection and visualization techniques
- Pipelines and column transformer (crucial topics often overlooked)
- Generalizing models to multiclass or multioutputs and probability calibration
- Deploying Scikit models with FastAPI and generating API docs

In this, many machine learning models covered in the lecture but not the lab assignments are demonstrated and analyzed along the way for comprehensiveness.

<img width="1291" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/f5470ee2-2bce-409b-bd98-184590d2c023">


See the `Scikit-learn Tutorials` folder to check out the tutorials.

</details>

<details closed>
<summary>
  <h2> 📷 Image Processing Tutorials </h2>
</summary>
<br>
  
Recognizing that many students lacked prior experience in image processing, an optional tutorial session was offered. This session focused on core image processing concepts derived from the course material, with a strong emphasis on hands-on practice and familiarization with image processing toolboxes.

✦ The series of tutorials cover the following using toolboxes such as OpenCV an Scikit-image:

  - Understanding and reading images with different toolboxes and related data structures/basic image features
  - Preprocessing images (greyscaling, contrast, equalization, thresholding, convolution, blur, edge detection, etc.)
  - Murphological methods (erosion, dilation, opening, closing, etc.)
  - Segmentation methods and object detection (clustering, region merging, hough transforms, etc.)
  - Texture analysis techniques (Local Binary Pattern, GLCM features, etc.)
  - Interest point detection (Harris Corner Detection, SIFT)

<img width="1062" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/9766e6a4-6201-40cc-aa54-4feeae545f7a">


See the `Image Processing Tutorials` folder to check out the tutorials.
</details>

<details closed>
<summary>
  <h2> 🚀 PyTorch Tutorials </h2>
</summary>
<br>
  
It was essential to familiarize students with deep learning frameworks and techniques because deep learning is a main component of this course. The main framework chosen for this was PyTorch.

✦ Students are first introduced to the deep learning cycle and the need of deep learning frameworks is motivated:

<img width="1096" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/a21e1bd6-9dc5-42c8-89a9-7f57ab9ed592">

Afterwards, PyTorch is broken down and then its main components are covered in a similar fashion to Scikit-learn:

<img width="1179" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/80034f98-0ee7-4d97-9c61-6f461c35ba5a">


**This includes the following topics:**

- PyTorch base functionality as a tensor processing package that is capable of automatic differentation and runs on the GPU 
- Implementing simple networks (linear and logistic regression) using only base functionality from PyTorch
- Dataloaders and datasets in PyTorch (as well as illustrating the need for `torchvision`, `torchaudio` and `torchtext`)
- Optimizers and schedulers in PyTorch
- Layers, loss functions and activations in PyTorch (including creating custom layers)
- Feedforward Neural Network on MNIST project
- Convolutional Neural Network on Hymenoptra (including fine-tuning)
- Spam SMS classifications with many-to-one RNNs

<img width="1062" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/e4dfe490-a199-4f20-91c2-1fad6e2929b7">


See the `PyTorch Tutorials` folder to check out the tutorials.
</details>

<details closed>
<summary>
  <h2> 💥 TensorFlow and Keras Tutorials </h2>
</summary>
<br>

This was presented as optional material for students willing to go beyond PyTorch, since in the industry it's common for corps to prefer only one over the other. We only briefly went over the material in the tutorial, contrary to PyTorch.

TensorFlow is broken down into main components:

<img width="1332" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/c506d624-e98d-4d0a-81b7-a9afaeb0b020">

Then Keras as well:
<img width="1090" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/22d34a6a-f76c-42f8-9d28-c007f767440b">


**This includes the following topics:**
- TensorFlow base functionality as a tensor processing package that is capable of automatic differentation and runs on the GPU
- TensorFlow VS. PyTorch discussion
- Loading and operating on data in TensorFlow
- High-level loading of data in Keras and using built-in datasets
- Layers (including custom ones) and loss functions in Keras
- Optimizers and schedulers in Keras
- Metrics in Keras
- KerasCV and KerasNLP Intro
- Sequential, Functional and Subclassing approaches to define models
- Callbacks in Keras
- Training and evaluating models at three different levels of abstractions
- Keras Ops and using PyTorch/Jax with Keras
- Feedforward Neural Network on MNIST project
- Convolutional Neural Network on Hymenoptra (including fine-tuning)
- Basic RNN use example

<img width="1062" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/34770014-36f1-40d7-9f9c-d68cc946ee33">


See the `TF Keras Tutorials` folder to check out the tutorials.
</details>

<details closed>
<summary>
  <h2> ⚗️ Lab Topics </h2>
</summary>
<br>
  
This section is only meant to further motivate you to take the course (i.e., labs will remain inaccessible). There are generally about six or seven labs where one lab typically takes the following form:
  
- Implementing machine learning technique(s) from scratch with OOP
- Testing the implementation by comparing to actual implementations from libraries
- Analyzing hyperparameter or properties of the technique (and comparing it with others when applicable)
- Using the technique over a real dataset in a full pipeline

Here are some lab highlights:

<img width="1313" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/91099331-0d82-4157-9787-ef5845e4dd3a">

<img width="1071" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/8e9db50e-0137-4fec-927d-7f5f80ac57eb">

<img width="1071" alt="image" src="https://github.com/EssamWisam/Applied-Machine-Learning-CU/assets/49572294/41fcee66-2e59-40bb-9d2d-0ec400bd8538">


</details>

<h2 align="center"> Thank You 💙</h2>
