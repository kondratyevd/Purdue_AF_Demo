When creating conda environments intended for use by multiple collaborators, it is advisable to use the procedure recommended by Purdue RCAC taking advantage of the [conda-env-mod](https://www.rcac.purdue.edu/knowledge/hammer/run/examples/apps/python/packages) command, and place the resulting module in a shared location from which all collaborators can access it.
Here's how the process looks like (compare to the [simple](https://github.com/piperov/Purdue_AF_Demo/blob/main/BuildYourOwnCondaEnvironment_simple.md) case):

```
  $ source /etc/profile.d/modules.sh
  $ module --force purge
  $ module load anaconda/2020.11-py38
  $ conda deactivate
  $ mkdir -p /depot/cms/conda_envs/spiperov/modules
  $ conda-env-mod create -p /depot/cms/conda_envs/spiperov/Coffea_DASK_pyROOT_ML -m /depot/cms/conda_envs/spiperov/modules --jupyter
  
```
At this point one needs to load the newly created module for this environment:

```
  $ module use /depot/cms/conda_envs/spiperov/modules
  $ module load conda-env/Coffea_DASK_pyROOT_ML-py3.8.8 
```
and then continue with adding the packages with conda:
```
  $ conda install root==6.24 root_numpy
  $ conda install coffea
  $ conda install dask[distributed] dask-jobqueue
  $ conda install pytest mplhep click correctionlib
  $ conda install uproot h5py matplotlib pandas 
  $ conda install tensorflow scikit-learn scikit-optimize
  $ conda install -c pytorch pytorch torchvision torchaudio cpuonly networkx ipywidgets tqdm vector  pyarrow
  $ conda install jupyterlab dask-labextension s3fs
  $ conda install nodejs
```
When finished, one can create a Jupyter 'kernel' file:
```
  $  conda-env-mod kernel -p /depot/cms/conda_envs/spiperov/Coffea_DASK_pyROOT_ML
Jupyter kernel created: "Python (My Coffea_DASK_pyROOT_ML Kernel)"

~/.local/share/jupyter/kernels/coffea_dask_pyroot_ml/kernel.json 
```
This kernel file contains a 'display_name' that can be changed to something descriptive - e.g.:
```
{
 "display_name": "Coffea_DASK_pyROOT_ML [AF]",
 ...
```
If now a coworker wants to use this new environment, they only need to load the two modules as above:
``` 
  $ module use /depot/cms/conda_envs/spiperov/modules 
  $ module load conda-env/Coffea_DASK_pyROOT_ML-py3.8.8
```
and if they wish to use the Jupyter kernel, they need to get a copy of the kernel.json file and place it in their 
```
~/.local/share/jupyter/kernels/
```
directory
