# [Synthetic video generation for autonomous vehicles](https://www.useloom.com/share/5f92e0aacbce41118e4fbf4d47d3ec33)
 
 :sassy_man: Don't want to read, watch a 6-min video :smiley: !
 
 [![](https://i.imgur.com/JjJj9CQ.png?1)](https://www.loom.com/embed/5f92e0aacbce41118e4fbf4d47d3ec33)
  
## Why I have selected this problem?
Statistically, each year up to 1.2 million deaths occur due to car accidents across the globe are caused by human errors. Autonomous vehicle technology could drastically avoid these accidents. Self-driving car companies are constantly trying to make their autonomous vehicles more robust by capturing a wide distribution of all possible driving scenarios but have failed to achieve at this point due to past recurring crashes. These autonomous systems actually learn from driving videos and the problem with currently available video datasets are
  1. Not annotated.
  2. Most of them aren't high-resolution videos which is again an impediment for object detection.

## What I am offering?   
An AI software solution with help of which you can:
1. Generate Semantic Segmentation Masks for existing videos.
<p float="left">
  <img src="https://github.com/anubhav0fnu/Synthetic-video-generation-for-Autonomous-cars/blob/master/results/gifs/reference_img/aachen_000000_000019_leftImg8bit.png" width="300" />
  <img src="https://github.com/anubhav0fnu/Synthetic-video-generation-for-Autonomous-cars/blob/master/results/gifs/reference_img/aachen_000000_000019_gtFine_color.png" width="300" /> 
</p>
2. Generate photo-realistic, high-resolution new driving videos.
<img src="https://github.com/anubhav0fnu/Synthetic-video-generation-for-Autonomous-cars/blob/master/results/gifs/CS_test2048Model_with_inst_fg_2048.gif" width="480" /> <br />

## How my Full Architechure looks like? 
It mainly constitutes of 3 components:
1. Video to frame sequence generator using OpenCV.
2. Generation of Semantic Segmentation masked frames for each associated frame sequences using [DEEPLAB](https://arxiv.org/abs/1606.00915) model. 
3. Generating new photo-realistic, high-resolution videos from the sequence of Semantic Segmentation masked frames using [conditional Generative Networks framework](https://arxiv.org/abs/1808.06601).

The full architecture: (Starting from LEFT to RIGHT.)
<img src="https://github.com/anubhav0fnu/Synthetic-video-generation-for-Autonomous-cars/blob/master/results/gifs/reference_img/full_archi.png" width="1000" /> <br />
