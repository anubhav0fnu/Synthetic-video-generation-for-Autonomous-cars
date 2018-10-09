#!/usr/bin/env bash

# Download the pre-trained Checkpoints and frozen inference graphs from :
# https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/model_zoo.md:

wget download.tensorflow.org/models/deeplabv3_cityscapes_train_2018_02_06.tar.gz
wget download.tensorflow.org/models/deeplab_cityscapes_xception71_trainfine_2018_09_08.tar.gz
wget download.tensorflow.org/models/deeplab_cityscapes_xception71_trainvalfine_2018_09_08.tar.gz

# ImageNet+ MS-COCO + {Cityscapes train_fine set}
tar -xzf deeplab_cityscapes_xception71_trainfine_2018_09_08.tar.gz
mv train_fine deeplab_cityscapes_xception71_trainfine_2018_09_08
rm deeplab_cityscapes_xception71_trainfine_2018_09_08.tar.gz

# pre-trained on ImageNet+ {Cityscapes train_fine set}
tar -xzf deeplabv3_cityscapes_train_2018_02_06.tar.gz
mv deeplabv3_cityscapes_train deeplabv3_cityscapes_train_2018_02_06
rm deeplabv3_cityscapes_train_2018_02_06.tar.gz


# ImageNet+ MS-COCO+ {Cityscapes trainval_fine and coarse set}
# This use to generate the test images.
tar -xzf deeplab_cityscapes_xception71_trainvalfine_2018_09_08.tar.gz
mv trainval_fine deeplab_cityscapes_xception71_trainvalfine_2018_09_08
rm deeplab_cityscapes_xception71_trainvalfine_2018_09_08.tar.gz


