import sys

import dask
from dask.distributed import Client
from dask.distributed import Scheduler, Worker
from dask_jobqueue import SLURMCluster

dask.config.set({"temporary-directory": "/tmp/spiperov/dask-temp/"})
dask.config.set({"distributed.worker.timeouts.connect": "60s"})

__all__ = [
    "pytest",
    "dask",
    "Client",
    "Scheduler",
    "Worker",
    "SLURMCluster",
    "dask_executor"
]

print("Dask version:", dask.__version__)

clusterA = SLURMCluster( project='cms', cores=1, memory='3.9GB',walltime='1-00:00:00', job_extra=['--qos=normal','--reservation=DASKTEST', '-o /tmp/dask_job.%j.%N.out','-e /tmp/dask_job.%j.%N.error'])
clusterA.adapt(minimum=10, maximum=100)
print(clusterA)

print("\nThe Dashboard of your DASK cluster is accessible at: ",clusterA.dashboard_link)
print("\nThis is the address of your DASK cluster, which you need to tell your DASK Client in the Jupyter Notebook:")
print(clusterA.scheduler_address)

