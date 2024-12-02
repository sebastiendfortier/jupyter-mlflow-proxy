# jupyter-mlflow-proxy

Jupyter server and notebook extension to proxy MLflow UI within JupyterLab/Jupyter Notebook. This extension allows you to access MLflow's UI directly from your Jupyter environment.

## Features

- Launch MLflow UI directly from JupyterLab launcher
- Seamless integration with JupyterHub authentication (if used)
- Simple, dependency-aware implementation
- No configuration needed - uses your existing MLflow installation

## Prerequisites

The following packages must be installed in your environment:
- JupyterLab or Jupyter Notebook
- MLflow and its dependencies
- jupyter-server-proxy

## Installation

### Using pip

```bash
pip install git+https://github.com/sebastiendfortier/jupyter-mlflow-proxy.git
```

### Using conda/mamba environment

Create a new environment using the provided `environment.yml`:

```bash
# If using conda
conda env create -f environment.yml

# If using mamba
mamba env create -f environment.yml
```

Then activate the environment:

```bash
conda activate mamba
```

## Usage

1. Start JupyterLab:
```bash
jupyter lab
```

2. Click on the MLflow icon in the Launcher tab
3. The MLflow UI will open in a new tab within JupyterLab

## Troubleshooting

If you encounter issues:

1. Verify MLflow is properly installed:
```bash
mlflow --version
```

2. Test MLflow UI directly:
```bash
mlflow ui
```

3. Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Development

Based on the [jupyter-server-proxy](https://jupyter-server-proxy.readthedocs.io/) framework.

## License

BSD 3-Clause License (see LICENSE file for details)
