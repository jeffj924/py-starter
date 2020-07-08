# settings.py
import dotenv
import os

# Create variables in .env file and load them here
# or set the values via environment variable
# ex.
# in .env file:
# PASSWORD="secret_password1"
# in settings.py file:
# password = os.getenv("PASSWORD")

script_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_path, '.env')
dotenv.load_dotenv(dotenv_path=env_path, verbose=True)

file_data = script_path + "\\test_data_files\\"


