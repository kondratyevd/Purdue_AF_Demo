#!/bin/bash


source /etc/profile.d/modules.sh
module --force purge 
module load anaconda/2020.11-py38  
conda deactivate                                                                                          
module use /depot/cms/conda_envs/cmslocal/modules                                                         
module load conda-env/Python_ML_DASK_GPU-py3.8.5  

# echo "use these to start your DASK cluster:"
# echo "clusterA = SLURMCluster( project='cms', cores=1, memory='3.9GB',walltime='1-00:00:00', job_extra=['--qos=normal','--reservation=DASKTEST', '-o /tmp/dask_job.%j.%N.out','-e /tmp/dask_job.%j.%N.error'])"
# echo "clusterA.adapt(minimum=10, maximum=100)"
# echo "print(clusterA)"

ipython -i slurm_cluster_prep.py 
