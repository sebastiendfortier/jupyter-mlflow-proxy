import os
import shutil
import sqlite3
from pathlib import Path
from traitlets import Unicode
from traitlets.config import LoggingConfigurable

class MLflowConfig(LoggingConfigurable):
    server_url = Unicode('', help='MLflow server URL').tag(config=True)

def get_icon_path():
    """Get the path to the MLflow icon"""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'mlflow.svg'
    )

def init_db():
    """Initialize SQLite database"""
    db_path = os.path.join(str(Path.home()), '.jupyter_mlflow.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mlflow_config
                 (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()
    return db_path

def store_mlflow_url(url):
    """Store MLflow URL in SQLite database"""
    db_path = os.path.join(str(Path.home()), '.jupyter_mlflow.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO mlflow_config (key, value) VALUES (?, ?)',
              ('server_url', url))
    conn.commit()
    conn.close()

def get_mlflow_url():
    """Get MLflow URL from SQLite database"""
    db_path = os.path.join(str(Path.home()), '.jupyter_mlflow.db')
    if not os.path.exists(db_path):
        return None
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT value FROM mlflow_config WHERE key = ?', ('server_url',))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def setup_mlflow():
    """Set up and return MLflow UI process configuration"""
    # Initialize the database
    init_db()
    
    def _get_cmd(port):
        """Get the MLflow UI command"""
        # Find mlflow executable in the current environment
        mlflow_path = shutil.which('mlflow')
        if not mlflow_path:
            raise FileNotFoundError('Could not find mlflow in PATH')

        server_url = f"http://localhost:{port}"
        message = f"MLflow server running on {server_url}"
        print(message)
        
        # Store URL in SQLite database
        store_mlflow_url(server_url)
        
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
