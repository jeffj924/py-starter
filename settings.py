# settings.py
import dotenv
import os
from pathlib import Path

dotenv.load_dotenv()
dotenv.load_dotenv(verbose=True)
env_path = Path('.') / '.env'
dotenv.load_dotenv(dotenv_path=env_path)

script_path = os.path.dirname(os.path.abspath(__file__))