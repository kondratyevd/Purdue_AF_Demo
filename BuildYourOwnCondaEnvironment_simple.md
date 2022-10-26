Conda environments are very big in volume, because they contain all the source code of the packages being install (including their dependencies). It is therefore best to store those outside of your home directory, which has a limited capacity.

RCAC's Data Depot is a very convenient location to store those, as it is available on all clusters, and the CMS group has a significant disk quota in it.

Every CMS user has a sub-directory `/depot/cms/conda_envs/<username>/` automatically created for the purposes of storing such environments.

Here is how your build process can look like. We will use the Coffea-HATS-2022 as an example:\
(this process makes use of the LMOD module management software on all RCAC clusters)\
(substitute "\<username\>" with your username as appropriate)
  ```
  $ source /etc/profile.d/modules.sh
  $ module --force purge
  $ module load anaconda/2020.11-py38
  $ conda deactivate
  $ conda create  --prefix /depot/cms/conda_envs/<username>/Coffea-HATS-2022 python=3.7
  $ conda activate /depot/cms/conda_envs/<username>/Coffea-HATS-2022
  $ conda install --prefix /depot/cms/conda_envs/<username>/Coffea-HATS-2022 coffea==0.7.13
  $ conda install --prefix /depot/cms/conda_envs/<username>/Coffea-HATS-2022 dask[distributed]
  $ conda install --prefix /depot/cms/conda_envs/<username>/Coffea-HATS-2022 ipykernel_launcher ipykernel
  ```

Once this process has succeeded, you can use your new environment by activating it first:
```
$ source /etc/profile.d/modules.sh
$ conda deactivate
$ module --force purge
$ module load anaconda/2020.11-py38
$ conda activate /depot/cms/conda_envs/<username>/Coffea-HATS-2022
```

If you want to make this environment available also in Jupyter Notebooks (as a new "kernel") you need to create a JSON file in 
```
~/.local/share/jupyter/kernels/
```
which tells Jupyter how to activate it.

A word of caution: Since Jupyter distinguishes available kernels by both their "display name" AND their relative location, it is advisable to name the directory which contains the JSON file in some unique way, so that it does not get "ghosted" by another kernel available in the standard system locations:

```
$ mkdir -p ~/.local/share/jupyter/kernels/Coffea-HATS-2022_<username>
```
and create a file named 
```
~/.local/share/jupyter/kernels/Coffea-HATS-2022_<username>/kernel.json
```
with contents like this:
```
{
 "display_name": "Coffea-HATS-2022 [<username>]",
 "language": "python3",
 "argv": [
  "/depot/cms/conda_envs/<username>/Coffea-HATS-2022/python_wrapper.sh",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ]
}
```
and finally create the python wrapper script:
```
/depot/cms/conda_envs/<username>/Coffea-HATS-2022/python_wrapper.sh
```
with these contents:
```
#!/bin/bash

source /etc/profile.d/modules.sh

module --force purge
module load anaconda/2021.05-py38

conda activate /depot/cms/conda_envs/<username>/Coffea-HATS-2022
exec python3 "$@"
```
and make it execurable:
`chmod +x /depot/cms/conda_envs/<username>/Coffea-HATS-2022/python_wrapper.sh`
