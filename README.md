# [Automated Turk: Enhancing Autonomous Vehicles]

Watch this video for an overview of the project:
https://www.useloom.com/share/5f92e0aacbce41118e4fbf4d47d3ec33

## Problem: Autonomous Vehicles Need Lots of Labeled High-Resolution Training Data
Each year across the globe, up to 1.2 million deaths associated with car accidents are caused by human error. Autonomous vehicle technology has the potential to drastically reduce these accidents. Self-driving car companies are constantly trying to make their autonomous vehicles more robust by capturing a wide distribution of possible driving scenarios. Past recurring crashes indicate that there is still substantial work to be done in this area. These autonomous systems learn from actual driving videos, collected with a human at the wheel. Several problems with currently available video datasets are:

1. Most of these videos are not annotated, and it is very expensive/time consuming to manually label them
2. Most training datasets are not high-resolution videos, which makes object detection more challenging/less robust
3. Driving videos are complex/difficult to augment, so the amount of training data is dependent on the collection of massive amounts of driving data. It is expensive/time consuming if a human driver with a complex sensor suite must be at the wheel for every second of the training data, so the dataset size is limited.

## Solution: An AI Software Package for Semantic Segmentation and Generation of High-Resolution Driving Videos
Part 1: Generate Semantic Segmentation Masks for existing videos
<p float="left">
  <img src="results/gifs/reference_img/aachen_000000_000019_leftImg8bit.png" width="300" />
  <img src="results/gifs/reference_img/aachen_000000_000019_gtFine_color.png" width="300" /> 
</p>
Part 2: Generate photo-realistic, high-resolution new driving videos to augment training
<img src="results/gifs/CS_test2048Model_with_inst_fg_2048.gif" width="480" /> <br />

## Full Architecture
The full architecture mainly consists of 3 components:
1. A video-to-frame sequence generator using OpenCV
2. Generation of Semantic Segmentation masked frames for each associated frame sequences using [DEEPLAB](https://arxiv.org/abs/1606.00915) model
3. Generation of new photo-realistic, high-resolution videos from the sequence of Semantic Segmentation masked frames using [conditional Generative Networks framework](https://arxiv.org/abs/1808.06601)

Full architecture diagram: (Read LEFT to RIGHT.)
<img src="results/gifs/reference_img/full_archi.png" width="1000" /> <br />

##### Brief description of the main directory structure.
| Folder/Files       | Description           |
| :------------- |:-------------| 
| **src**      | Contains the main components of the architecture
| **src/data_prepration**     | Scripts for cutting videos into frames using openCV       |
| **src/semantic_seg_gen**  | Generates semantic segmentation masked frames      |
| **src/synthetic_video_gen** | Generates new synthetic RGB frames      |
| **results** | stiched frames in the form of gifs      |
| **docker** | Dockerfile to run the complete project as a standalone application in a container (work in progress)      |
| **datasets** |  Samples of BDD & Citycapes datasets used in the project      |
| **utility** | python implementation of useful decorators (to assist development)      |
| **README.md** | Overview of the project & guide to using this codebase       |

### Diving into the codebase:

##### Pre-Requisites:
AWS cloud sources were used for implementation and training/testing/validation of models. The [Deep Learning AMI (Ubuntu)](https://aws.amazon.com/marketplace/pp/B077GCH38C) provided stable pre-intalled conda environments for `TensorFlow 1.10.0` & `PyTorch 0.4.1` with `CUDA 9.0`. First time users of AWS could use [this](https://docs.google.com/document/d/1v1SKwaa_nuFD2cpKmDFUHf66YQTTEpv80aus3g4yFP4/edit?ts=5b96f8e6) to set up their environment.

The p2.xlarge instance was used for second component & p3.2xlarge instance for third component, as described below.

| EC2-instance size        | GPUs        | GPU Memory (GB)  |
| ------------- |:-------------| :-----|
| [p2.xlarge](https://aws.amazon.com/ec2/instance-types/p2/)      | 1 (NVIDIA K80) | -- |
| [p3.2xlarge](https://aws.amazon.com/ec2/instance-types/p3/)      | 1 (NVIDIA Tesla V100)      |   16 |

An S3 bucket was used for data dumps via a [python script](src/data_prepration/data_BDD100K2S3.py). You could also leverage [my hacks](https://gist.github.com/anubhav0fnu/3d4f6a3c9ce1342fb1d3671613150b65) & different IDE integration options [here](https://stackoverflow.com/questions/52340973/is-it-possible-to-ssh-in-aws-instances-using-any-ides-such-pycharm/52378438#52378438) to quickly get started working with cloud sources on a local workstation.

##### Setting it up!
Once you have set up your AWS AMI for an EC2 instance, ssh into the machine and follow the instructions, below:

**Installation**:

Switch to tensorflow_p36 conda environment & install : 
> **Component 1**:
opencv
pillow
```python
pip install opencv-python
pip install Pillow==2.2.1
```

> **Component 2**:
tf Slim ( It picks up the binaries from tensorflow installation!)

jupyter notebook (Needed for quick visualization.)

```python
conda install -c anaconda jupyter
```

Now, switch to pytorch_p36 conda environment & install : 
> **Component 3**:

[dominate](https://github.com/Knio/dominate) 
```python
pip install dominate requests
```
Download and compile a snapshot of FlowNet2 by running:

```python
python src/synthetic_video_gen/scripts/download_flownet2.py
```

**NOTE**: Coming soon: I will be providing a dockerfile that will take care of your environment & repository setup in a docker container, as explained above.

### Component 1: Data prepration.
`src/data_prepration/data_prep.py`

This script uses `OpenCV` to cut videos in to frames and save it into the desired folder. 

### Component 2: Semantic Segmentation mask generation.

The below directory structure is needed for `src/semantic_seg_gen` because it contains deeplab code & datasets in TFrecord format. For this component, I have used a well documented pre-existing implementation of [deeplab](https://github.com/tensorflow/models/tree/master/research/deeplab). 

As GitHub doesn't support large files, I have written extra instructions while describing the directory structure. Datasets, models, and frozen graphs can be downloaded using [this script](src/semantic_seg_gen/download_data_in_dir.sh). 

---
```bash
semantic_seg_gen
├── bdd100k (dataset-1)
│   ├── bdd100kscripts
│   ├── checkpoints
│   ├── exp (create these directories, required by deeplab scripts.)
│   │   └── train_on_train_set
│   │       ├── test
│   │       ├── train
│   │       └── val
│   ├── images
│   ├── labels
│   └── tfrecord
├── build_cityscapes_data.py (find scripts at "https://github.com/tensorflow/models/tree/master/research/deeplab/datasets/")
├── build_data.py
├── cityscapes (dataset-2)
│   ├── checkpoints
│   │   └── deeplabv3_cityscapes_train
│   ├── cityscapesscripts (maintain hierarchy, git clone "https://github.com/mcordts/cityscapesscripts.git")
│   │   ├── annotation
│   │   ├── evaluation
│   │   ├── helpers
│   │   ├── preparation
│   │   └── viewer
│   ├── exp
│   │   └── train_on_train_set
│   │       ├── eval
│   │       ├── train
│   │       └── vis
│   │           ├── raw_segmentation_results
│   │           └── segmentation_results
│   ├── gtfine (login & download the "gtfine_trainvaltest.zip" dataset)
│   │   ├── test
│   │   ├── train
│   │   └── val
│   ├── leftimg8bit (login & download the "leftimg8bit_trainvaltest.zip" dataset)
│   │   ├── test
│   │   ├── train
│   │   └── val
│   └── tfrecord (filled by "convert_cityscapes.sh" script.)
├── convert_cityscapes.sh (split data into train & val sets & converts totfrecords's shards.)
├── deeplab ( git clone https://github.com/tensorflow/models/blob/master/research/deeplab)
│   └── ...
├── deeplab_train_1.sh (script to run deeplab/train.py)
├── deeplab_eval_1.sh   (script to run deeplab/eval.py)
├── deeplab_vis_1.sh   (script to run deeplab/vis.py)
└── download_data_in_dir.sh (after creating above directory structure, could be used for populating directories.)
```
---

The deeplab implementation is in tensorflow, and we need to first convert our dataset into TFrecord. You can use [this script](src/semantic_seg_gen/convert_cityscapes.sh) for this purpose. Once you have your dataset in the proper format, start with training and evaluation.

The second frozen checkpoint that was used for evaluation and comparison of results among other 3 will be posted [here]() soon.

---
| Number| checkpoint name | pre-trained dataset  |
| :------------- | :------------- |:-------------|
|1 | deeplab_cityscapes_xception71_trainfine    | ImageNet+ MS-COCO + {Cityscapes train_fine set} |
|2 | deeplabv3_cityscapes_train    | ImageNet+ {Cityscapes train_fine set}      |      
|3 | deeplab_cityscapes_xception71_trainvalfine     | ImageNet+ MS-COCO+ {Cityscapes trainval_fine and coarse set}

---


**Training**:

`src/semantic_seg_gen/deepLab_train_1.sh`

This is the local training job using the `xception_65` model. I have highlighted some of the problems I ran into during training in the comments within the script.


**Evaluation**:

Later, using the latest checkpoint collected in `src/semantic_seg_gen/cityscapes/exp/train_on_train_set/train/train_00_result` directory, we can generate the semantic masks for our sequence of images.


### Component 3: Video Synthesis using a Conditional GAN
Once we have our `labels` a.k.a `Semantic Segmentation Masks (SSM)` available for our videos (sequences of frames), we can start with:

**Training**:

For a single GPU, use

`src/synthetic_video_gen/scripts/street/test_g1_1024.sh`

For multiple GPUs use

`src/synthetic_video_gen/scripts/street/train_2048.sh`

**Testing**: 

For a single GPU, use

`src/synthetic_video_gen/scripts/street/test_g1_1024.sh`

For multiple GPUs use

`src/synthetic_video_gen/scripts/street/test_2048.sh`

The videos, below, show results of video synthesis at two scales: medium (1024) and fine (2048) resolution. In each category the "Before" video shows the initial results based on 3 inputs to the sequential generator: `current (SSM)`, `previous 2 SSMs`, `previous 2 generated synthetic frames`. The "After" video shows improved results with the addition of a 4th input to the generator, which is the `foreground feature` of the input SSM's. 

#### Medium (scale: 1024) Trained Generator Model.
##### Before

<img src="results/gifs/CS_test1024Model_without_inst_fg_1024.gif" width="480" /> <br />

##### After

<img src="results/gifs/CS_test2048Model_with_inst_fg_1024.gif" width="480" /> <br />

#### Fine (scale: 2048) Trained Generator Model.

##### Before

<img src="results/gifs/CS_test2048Model_without_inst_fg_2048.gif" width="480" /> <br />

##### After

<img src="results/gifs/CS_test2048Model_with_inst_fg_2048.gif" width="480" /> <br />

### Future Steps:
I plan to continue developing on top of the current codebase. Contributions are welcome. Please feel free to add your own features or implement something from the list, below.

Some of my ideas for improvement are:

1. Adding support for Multi-modal synthesis & semantic Manipulation techniques to generate rare events in the videos
2. Perfoming a Joint training of the two Neural networks (DeepLab NN + Conditional Generative adverserial NN)
3. Adding support of [CARLA: An Open Urban Driving Simulator](http://carla.org/) in order to evaluate the newly-generated synthetic videos within a self-driving car environment. I need to override my dataset as an input to their simulator
4. Benchmarking the results from the current approach with others such as PIX-2-PIXHD & COVST approaches
5. Coming up with an Evaluation metric!

**Credits: I would like to thank the authors for providing [vid2vid](https://github.com/NVIDIA/vid2vid) framework in pyTorch and [DeepLab](https://github.com/tensorflow/models/tree/master/research/deeplab) implementation in tensorFlow.  
