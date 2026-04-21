#!/bin/bash

python3 main.py \
--seed 1 \
--log_group simplenet_mvtec \
--log_project MVTecAD_Results \
--results_path results \
--run_name runAug \
net \
-b wideresnet50 \
-le layer2 \
-le layer3 \
--pretrain_embed_dimension 1536 \
--target_embed_dimension 1536 \
--patchsize 3 \
--meta_epochs 40 \
--embedding_size 256 \
--gan_epochs 4 \
--noise_std 0.015 \
--dsc_hidden 1024 \
--dsc_layers 2 \
--dsc_margin .5 \
--pre_proj 1 \
dataset \
--batch_size 4 \
--resize 329 \
--rotate_degrees 5 \
--translate 0.02 \
--scale 0.02 \
--brightness 0.05 \
--contrast 0.05 \
--saturation 0.05 \
--gray 0.0 \
--hflip 0.5 \
--vflip 0.0 \
--imagesize 288 \
-d sleeve \
mvtec \
./data
