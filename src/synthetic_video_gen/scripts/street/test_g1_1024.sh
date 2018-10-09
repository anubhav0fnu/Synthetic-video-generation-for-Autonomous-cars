#!/usr/bin/env bash

#bash ./scripts/street/test_g1_1024.sh

# for CityScape
#with inst + fg
#python test.py --name label2city_1024_g1 --label_nc 35 --loadSize 1024 --n_scales_spatial 3 --use_instance --fg --n_downsample_G 2 --use_single_G

#without inst +fg --> quality degrades.
#python test.py --name label2city_1024_g1 --label_nc 35 --loadSize 1024 --n_scales_spatial 3 --n_downsample_G 2 --use_single_G


# for BDD100K

# this fails as valueError: Single image generator does not exist , and
# without "--use_single_G" it complains for ValueError: Please specify the method for generating the first frame
#python test.py --name label2city_1024_g1 --dataroot datasets/BDD/ --label_nc 40 --loadSize 720 \
#--n_scales_spatial 3 --n_downsample_G 2 --use_single_G

python test.py --name label2city_1024_g1 --dataroot datasets/BDD/ --label_nc 40 --loadSize 1280 \
--n_scales_spatial 3 --n_downsample_G 2 --use_real_img

#python test.py --name label2city_1024_g1 --dataroot datasets/BDD/ --label_nc 40 --loadSize 736 \
# --n_scales_spatial 3 --use_instance --fg --n_downsample_G 2 --use_single_G
