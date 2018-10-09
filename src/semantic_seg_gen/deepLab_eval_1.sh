#!/usr/bin/env bash

#  path to the trained checkpoint
PATH_TO_CHECKPOINT="cityscapes/exp/train_on_train_set/train/train_2_result"

#  directory in which evaluation events will be written
PATH_TO_EVAL_DIR="cityscapes/exp/train_on_train_set/eval"
#  directory in which the Cityscapes dataset resides
PATH_TO_DATASET="cityscapes/tfrecord"

# From tensorflow/models/research/
python deeplab/eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --eval_crop_size=1025 \
    --eval_crop_size=2049 \
    --dataset="cityscapes" \
    --checkpoint_dir=${PATH_TO_CHECKPOINT} \
    --eval_logdir=${PATH_TO_EVAL_DIR} \
    --dataset_dir=${PATH_TO_DATASET}

