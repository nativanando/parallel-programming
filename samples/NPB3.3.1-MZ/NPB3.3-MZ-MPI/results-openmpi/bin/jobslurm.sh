#!/bin/bash

# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename

#SBATCH --time=20:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=4   # number of nodes
#SBATCH --ntasks-per-node=8   # 4 processor core(s) per node
#SBATCH --job-name="nativa-jobs"
#SBATCH --output="slurm-%j.out.log" # job standard output file (%j replaced by job id)
#SBATCH --error="slurm-%j.err.out.log" # job standard error file (%j replaced by job id)
# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE

mpiexec --hostfile machines --allow-run-as-root bt-mz.D.32

