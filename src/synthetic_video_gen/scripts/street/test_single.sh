#!/usr/bin/env bash

#bash ./scripts/street/test_single.sh

# Hwo to test this
python test.py --name label2city_single --label_nc 35 --loadSize 512 \
--n_scales_spatial 3 --use_instance --fg --n_downsample_G 2 --use_single_G

#python test.py --name label2city_single --label_nc 35 --loadSize 1024 \
#--n_scales_spatial 3 --use_instance --fg --n_downsample_G 2 --use_single_G