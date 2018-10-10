#!/usr/bin/env bash

#  path to the trained checkpoint
PATH_TO_CHECKPOINT="cityscapes/exp/train_on_train_set/train/train_2_result"
#  directory in which evaluation events will be written
PATH_TO_VIS_DIR="cityscapes/exp/train_on_train_set/vis"
#  directory in which the Cityscapes dataset resides
PATH_TO_DATASET="cityscapes/tfrecord"

python deeplab/vis.py \
    --logtostderr \
    --vis_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size=1025 \
    --vis_crop_size=2049 \
    --dataset="cityscapes" \
    --colormap_type="cityscapes" \
    --also_save_raw_predictions = True \
    --checkpoint_dir=${PATH_TO_CHECKPOINT} \
    --vis_logdir=${PATH_TO_VIS_DIR} \
    --dataset_dir=${PATH_TO_DATASET}