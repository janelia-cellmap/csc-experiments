#!/bin/bash
# rm logs/*

# export CUDA_LAUNCH_BLOCKING=1 # for debugging
export SEED=$2

bsub -J "t_$1" -n 12 -gpu "num=1" -q gpu_h100 -e "logs/train_$1_$(date +%Y%m%d%H%M%S).err" -o "logs/train_$1_$(date +%Y%m%d%H%M%S).out" python "train_$1.py"