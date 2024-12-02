import os
import shutil
import getpass
from pathlib import Path

def get_mlflow_executable():
    """Find mlflow executable in known locations"""
    if shutil.which('mlflow'):
        return 'mlflow'
    
    raise FileNotFoundError('Could not find mlflow in PATH')

def get_icon_path():
    """Get the path to the MLflow icon"""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'mlflow.svg'
    )

def setup_mlflow():
    """Set up and return MLflow UI process configuration"""
    def _get_env(port):
        """Get environment variables for MLflow"""
        return {
            'MLFLOW_TRACKING_URI': f'http://localhost:{port}',
            'USER': os.getenv('NB_USER', getpass.getuser())
        }

    def _get_cmd(port):
        """Get the MLflow UI command"""
        # Create a default directory for MLflow artifacts if it doesn't exist
        artifact_path = os.path.expanduser('~/mlflow-artifacts')
        Path(artifact_path).mkdir(parents=True, exist_ok=True)

        cmd = [
            get_mlflow_executable(),
            'ui',
            '--host=127.0.0.1',
            f'--port={port}',
            f'--backend-store-uri={artifact_path}'
        ]
        return cmd

    def _get_timeout(default=120):
        """Get UI timeout in seconds"""
        try:
            return float(os.getenv('MLFLOW_TIMEOUT', default))
        except Exception:
            return default

    server_process = {
        'command': _get_cmd,
        'timeout': _get_timeout(),
        'environment': _get_env,
        'launcher_entry': {
            'title': 'MLflow',
            'icon_path': get_icon_path()
        }
    }
    return server_process 
