import setuptools

setuptools.setup(
    name="jupyter-mlflow-proxy",
    version='1.0.0',
    url="https://github.com/sebastiendfortier/jupyter-mlflow-proxy",
    author="Original: Ryan Lovett & Yuvi Panda",
    description="Jupyter extension to proxy MLflow",
    packages=setuptools.find_packages(),
    keywords=['Jupyter', 'MLflow'],
    classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.2.3,!=4.0.0,!=4.1.0',
        'mlflow>=2.8.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'mlflow = jupyter_mlflow_proxy:setup_mlflow'
        ]
    },
    package_data={
        'jupyter_mlflow_proxy': ['icons/mlflow.svg'],
    },
)
