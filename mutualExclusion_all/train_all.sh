# Loop over all train_*.py files in the experiments/generalist/base_2024 directory and run them with the specified seed and port. Increment the port by 1 for each run.

# rm logs/*
seed=$1

for file in train_*.py; do
    # Extract train_<model>.py from file
    model=$(echo $file | cut -d'_' -f2 | cut -d'.' -f1)
    echo Training $model with seed $seed
    rm logs/train_$model*
    sh train.sh $model $seed
done
