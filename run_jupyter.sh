#!/bin/bash --login
#SBATCH --time=08:00:00
#SBATCH --partition Short
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

port=2718  # use this port on local, login and compute machines
conda_env_name="open-gira"

##########
# README #
##########
#
# F. Thomas 20240829
#
# This SLURM job submission script runs a jupyter notebook server on a OUCE
# cluster compute node.
#
# Inspired by: https://evcu.github.io/notes/port-forwarding/
#
# To use:
#
# 1  Connect to OUCE cluster with:
#    $ ssh -L <port>:localhost:<port> <username>@ouce-hn01.ouce.ox.ac.uk
#
# 2a Modify this script:
#    - sbatch job/resource parameters
#    - port choice (anything unused in the range 2000-65000)
#    - conda environment name
#
# 2b Submit this script as a job with:
#    $ sbatch run_jupyter.sh
#
# 3  Check the job logs to see output from the jupyter server with:
#    $ tail -f slurm-<job_id>.out
#    N.B. The jupyter server can take a minute or tw to be ready
#
# 4  To connect from your local machine, wait for the logs to show a line like:
#       http://localhost:<port_compute>/?token=<long_uuid>
#       ... and open this in your browser

#######
# JOB #
#######

# reverse tunnel back to login node
#
#   for this to work (without password authentication), you will need to have added
#   a public key of yours on the cluster to the authorised hosts file on the cluster
#       e.g. to create a new key, from the login node, run:
#           $ ssh-keygen -t ed25519
#       then append contents of new key to authorized_keys file:
#           $ cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
ssh -N -f -R $port:localhost:$port ouce-hn01.ouce.ox.ac.uk

# start jupyter server from within a specified conda environment
# this should run until cancelled or the job hits its time limit
micromamba run -p ~/micromamba/envs/$conda_env_name jupyter notebook --no-browser --port $port
