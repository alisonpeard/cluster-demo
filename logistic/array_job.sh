#! /bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
#SBATCH --time=00:10:00
#SBATCH --partition=Short
#SBATCH --mail-type=END,FAIL
#SBATCH --array=0-99

hostname
date
micromamba run --name demo python logistic_map_zoom.py $SLURM_ARRAY_TASK_ID
