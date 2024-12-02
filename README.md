# jupyter-mlflow-proxy

Jupyter server and notebook extension to proxy MLflow UI within JupyterLab/Jupyter Notebook.

## Features

- Launches MLflow UI server within your Jupyter environment
- Automatically configures MLflow tracking URI
- Provides a default local artifact store
- Seamless integration with JupyterHub authentication (if used)

## Installation

### Prerequisites

Install MLflow:
```bash
pip install mlflow
```

### Install jupyter-mlflow-proxy

Install via pip:
```bash
pip install jupyter-mlflow-proxy
```

## Configuration

The following environment variables can be used to configure the proxy:

| Environment Variable | Description | Default Value |
|---------------------|-------------|---------------|
| MLFLOW_TIMEOUT | Server timeout in seconds | 120 |
| NB_USER | Fallback username if system user lookup fails | System user |

## Usage

1. Start JupyterLab or Jupyter Notebook
2. Click on the MLflow icon in the launcher
3. The MLflow UI will open in a new tab

The MLflow tracking URI will be automatically set to the proxied server URL. Artifacts are stored by default in `~/mlflow-artifacts`.

## Development

Based on the [jupyter-server-proxy](https://jupyter-server-proxy.readthedocs.io/) framework.
