from IPython.display import display, Javascript
import os
import shutil

def get_icon_path():
    """Get the path to the MLflow icon"""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'mlflow.svg'
    )

def setup_mlflow():
    """Set up and return MLflow UI process configuration"""
    def _get_cmd(port):
        """Get the MLflow UI command"""
        # Find mlflow executable in the current environment
        mlflow_path = shutil.which('mlflow')
        if not mlflow_path:
            raise FileNotFoundError('Could not find mlflow in PATH')

        message = f"MLflow server running on http://localhost:{port}"
        print(message)
        
        return [
            mlflow_path,
            'ui',
            '--port', str(port),
            '--host', '0.0.0.0'
        ]

    return {
        'command': _get_cmd,
        'absolute_url': False,
        'launcher_entry': {
            'title': 'MLflow',
            'icon_path': get_icon_path(),
            'notification': 'MLflow server is starting...'
        },
        'timeout': 90,           # Timeout in seconds
        'new_browser_tab': True  # Opens in a new tab
    } 
