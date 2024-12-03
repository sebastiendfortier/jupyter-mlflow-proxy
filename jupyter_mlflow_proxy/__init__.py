import os
import shutil
from jupyter_server.serverapp import ServerApp
from traitlets import Unicode
from traitlets.config import LoggingConfigurable

class MLflowConfig(LoggingConfigurable):
    server_url = Unicode('', help='MLflow server URL').tag(config=True)

def get_icon_path():
    """Get the path to the MLflow icon"""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'mlflow.svg'
    )

def setup_mlflow():
    """Set up and return MLflow UI process configuration"""
    mlflow_config = MLflowConfig()
    
    def _get_cmd(port):
        """Get the MLflow UI command"""
        # Find mlflow executable in the current environment
        mlflow_path = shutil.which('mlflow')
        if not mlflow_path:
            raise FileNotFoundError('Could not find mlflow in PATH')

        server_url = f"http://localhost:{port}"
        message = f"MLflow server running on {server_url}"
        print(message)
        
        # Store URL in multiple places for accessibility
        os.environ['MLFLOW_SERVER_URL'] = server_url
        mlflow_config.server_url = server_url
        
        # If running in a Jupyter context, set server config
        try:
            server_app = ServerApp.instance()
            if server_app:
                server_app.config.MLflowConfig.server_url = server_url
                print(f"Server app config: {server_app.config}")
                print(f"Config location: {server_app.config_file_paths}")
        except Exception as e:
            print(f"Error setting server config: {e}")
        
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
            'icon_path': get_icon_path()
        },
        'timeout': 90,           # Timeout in seconds
        'new_browser_tab': True  # Opens in a new tab
    } 
