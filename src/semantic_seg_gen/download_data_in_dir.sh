#!/usr/bin/env bash


#Download Models, datasets, scripts for  a new user into the appropriate directory.
#Assumption, the user has followed & created empty directory structure mentioned in README.

CURRENT_DIR=$(pwd)
WORK_DIR="."

PROJECT_ROOT="${WORK_DIR}/"

BBD_SCRIPTS="${WORK_DIR}/bdd100K/bdd100kscripts"
echo "Downloading BBD_SCRIPTS from github"
cd BBD_SCRIPTS
git clone https://github.com/ucbdrive/bdd-data.git
cd bdd_data
mv * ../../
rm bdd_data
cd "${PROJECT_ROOT}"

CITYSCAPES_SCRIPTS="${WORK_DIR}/cityscapes/cityscapesscripts"
echo "Downloading CITYSCAPES_SCRIPTS from github"
git clone https://github.com/mcordts/cityscapesScripts.git
cd cityscapesscripts
mv * ../../
rm cityscapesScripts
cd "${PROJECT_ROOT}"


echo "populating the initial checkpoint for cityScapes dataset."
CITYSCAPES_PRETRAINED_CKPT="${WORK_DIR}/cityscapes/checkpoints"
cd CITYSCAPES_PRETRAINED_CKPT
# Now, download the pre-trained checkpoint: "xception_cityscapes_trainfine"
# checkpoints that have been pretrained on ImageNet + Cityscapes train_fine set.
wget download.tensorflow.org/models/deeplabv3_cityscapes_train_2018_02_06.tar.gz
tar -xzf deeplabv3_cityscapes_train_2018_02_06.tar.gz
rm deeplabv3_cityscapes_train_2018_02_06.tar.gz
echo "this would be your initial ckpt to start with"
echo "${CITYSCAPES_PRETRAINED_CKPT}"
cd "${PROJECT_ROOT}"

echo "Downloading the cityscapes gtFine_trainvaltest.zip dataset"
CITYSCAPES_GTFINE="${WORK_DIR}/cityscapes/gtFine"
cd CITYSCAPES_GTFINE
wget https://www.cityscapes-dataset.com/file-handling/?packageID=1
tar -xzf gtFine_trainvaltest.zip
rm gtFine_trainvaltest.zip
cd "${PROJECT_ROOT}"

echo "Downloading the cityscapes leftImg8bit_trainvaltest.zip dataset"
CITYSCAPES_LEFTIMG8BIT="${WORK_DIR}/cityscapes/leftImg8bit"
cd CITYSCAPES_LEFTIMG8BIT
wget https://www.cityscapes-dataset.com/file-handling/?packageID=3
tar -xzf leftImg8bit_trainvaltest.zip
rm gtFine_leftImg8bit_trainvaltest.zip
cd "${PROJECT_ROOT}"

