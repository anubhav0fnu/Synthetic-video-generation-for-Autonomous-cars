#!/usr/bin/env bash

python test.py --name label2city_512_g1 --label_nc 35 --loadSize 512 \
--n_scales_spatial 3 --use_instance --fg --n_downsample_G 2 --use_single_G

python test.py --name label2city_512_g1 --label_nc 35 --loadSize 1024 \
--n_scales_spatial 3 --use_instance --fg --n_downsample_G 2 --use_single_G


#--use_single_G
