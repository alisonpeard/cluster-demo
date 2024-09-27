#!/bin/bash --login

#SBATCH --job-name=hostname_test
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1gb
#SBATCH --time=0-00:05:00
#SBATCH --partition=Short
#SBATCH --mail-type=END,FAIL

micromamba run --name demo python mandelbrot.py
