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
