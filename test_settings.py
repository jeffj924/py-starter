# test_settings.py
import dotenv
import os

test_script_path = os.path.dirname(os.path.abspath(__file__))
test_env_path = os.path.join(test_script_path, '.testenv')
dotenv.load_dotenv(dotenv_path=test_env_path, verbose=True)

test_file_data = test_script_path + "\\z_test_data_files\\"
my_secret_test_password = os.getenv("SECRET_TEST_PASSWORD")
