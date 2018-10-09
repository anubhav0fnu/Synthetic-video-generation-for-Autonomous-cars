# Automated Turk: Enhancing Autonomous Vehicles.
Statistically, each year up to 1.2 million deaths that occur due to car accidents across the globe were caused by human errors. Autonomous vehicle technology could drastically avoid these accidents. The self-driving car companies constantly trying to make their autonomous vehicles more robust by capturing the wide distribution of all possible driving scenarios but they failed   to achieve at this point due to past recurring crashes. These autonomous systems actually learn from driving videos and the problem with currently available video datasets are
  1. Not annotated.
  2. Most of them aren't high resolution videos which is again an impediment for object detection.
   
So, this is an AI software solution with help of which you can:
1. Generate Semantic Segmention Masks for existing videos.

<p float="left">
  <img src="results/gifs/hyperlink_img/aachen_000000_000019_leftImg8bit.png" width="300" />
  <img src="results/gifs/hyperlink_img/aachen_000000_000019_gtFine_color.png" width="300" /> 
</p>

2. Generate photo-realistic, High-resolution new driving videos.
<img src="results/gifs/CS_test2048Model_with_inst_fg_2048.gif" width="480" /> <br />

#### Full architechure
It will help the user to understand the flow of the code.

<img src="results/gifs/hyperlink_img/full_archi.png" width="1000" /> <br />

#### a list of files contained in the repository with a brief description of each file

#### a list of files contained in the repository with a brief description of each file
* **src** &#160; &#160;: Contains the main components of the architecture.
* **src/data_prepration** &#160; &#160;: Video cutting using openCV 
* **src/semantic_seg_gen**  &#160; &#160;: Generates semantic segmentation masked frames. 
* **src/synthetic_video_gen** &#160; &#160;          : Generates synthetic RGB frames.
* **results** &#160; &#160;   : stiched frames in gifs
* **docker** &#160; &#160;           : Dockerfile to run the complete project as standalone application in a container(work in progress)
* **datasets** &#160; &#160;   : Snippets of the BDD & Citycapes datasets used in the project.
* **tests**  &#160; &#160;            : Evaluation scripts(work in progress)
* **README.md**   &#160; &#160;          : Overview of the project & How to guide to use this codebase. 



#### Directory structure needed for src/semantic_seg_gen.
- Include instructions of how to launch scripts in the build subfolder
Create the following directory structure for obtaining the Semantic Segmentation Masked images : 
---
```bash
ssm_generation
├── bdd100K (dataset-1)
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
│   ├── cityscapesscripts (Maintain hierarchy, git clone "https://github.com/mcordts/cityscapesScripts.git")
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
│   ├── gtFine (Login & download the "gtFine_trainvaltest.zip" dataset)
│   │   ├── test
│   │   ├── train
│   │   └── val
│   ├── leftImg8bit (Login & download the "leftImg8bit_trainvaltest.zip" dataset)
│   │   ├── test
│   │   ├── train
│   │   └── val
│   └── tfrecord (Filled by "convert_cityscapes.sh" script.)
├── convert_cityscapes.sh (split data into train & val sets & converts toTFrecords's shards.)
├── deeplab ( git clone https://github.com/tensorflow/models/blob/master/research/deeplab)
│   └── ...
├── deepLab_train_1.sh (script to run deeplab/train.py)
├── deepLab_eval_1.sh   (script to run deeplab/eval.py)
├── deepLab_vis_1.sh   (script to run deeplab/vis.py)
└── download_data_in_dir.sh (After creating above directory structure, could be used for populating directories.)
```


#### Medium(scale: 1024) trained “G” model.
##### Before

<img src="results/gifs/CS_test1024Model_without_inst_fg_1024.gif" width="480" /> <br />

##### After

<img src="results/gifs/CS_test2048Model_with_inst_fg_1024.gif" width="480" /> <br />

#### Fine (scale: 2048) trained “G” model.

##### Before

<img src="results/gifs/CS_test2048Model_without_inst_fg_2048.gif" width="480" /> <br />

##### After

<img src="results/gifs/CS_test2048Model_with_inst_fg_2048.gif" width="480" /> <br />

