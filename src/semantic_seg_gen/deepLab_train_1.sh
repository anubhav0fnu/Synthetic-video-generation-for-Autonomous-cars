#!/usr/bin/env bash

#  path to the initial checkpoint- a ImageNet pretrained checkpoint.
PATH_TO_INITIAL_CHECKPOINT="cityscapes/checkpoints/deeplabv3_cityscapes_train_2018_02_06/model.ckpt.data-00000-of-00001"
#  directory in which training checkpoints and events will be written.
PATH_TO_TRAIN_DIR="cityscapes/exp/train_on_train_set/train/train_0_result"
#  directory in which the Cityscapes dataset resides.
PATH_TO_DATASET="cityscapes/tfrecord"

python deeplab/train.py \
    --logtostderr \
    --training_number_of_steps=90000 \
    --fine_tune_batch_norm=false \
    --train_split="train" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size=769 \
    --train_crop_size=769 \
    --train_batch_size=2 \
    --dataset="cityscapes" \
    --tf_initial_checkpoint=${PATH_TO_INITIAL_CHECKPOINT} \
    --train_logdir=${PATH_TO_TRAIN_DIR} \
    --dataset_dir=${PATH_TO_DATASET}



# Commann errors encountered , Stay PUT :) !!
#0. No data files found in train-*
#Soln:
#    Look in to your tfrecord folder for each dataset, you are supposed to chunk out your dataset into different sharads which is in TFrecord format.!
#1. Error reported to Coordinator: Nan in summary histogram
#Soln:
#    --fine_tune_batch_norm=false
#2. ResourceExhaustedError (see above for traceback): OOM when allocating tensor with shape[2304,195,195] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc
#Soln:
#    reduce the training batch size:
#    -train_batch_size=1

