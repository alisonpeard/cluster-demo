#! /bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=0-00:05:00
#SBATCH --partition=Short
#SBATCH --mail-type=END,FAIL

echo "hello, world"
hostname
date
