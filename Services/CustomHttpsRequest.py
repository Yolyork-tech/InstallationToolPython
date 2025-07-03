import requests
import requests as http
import os

from Services.CustomLogger import log_to_file
from Services.HtmlParsing import find_latest_file_url

def http_request(app_name, app_data):
    """
    Download a list of applications
    :param app_name:
    :param app_data:
    :return:
    """
    try:
        url = app_data['Url']
        temp_dir = os.environ["TEMP"]
        os.makedirs(os.path.join(temp_dir, "utils"), exist_ok=True)
        save_path = os.path.join(temp_dir, "utils", app_data["RegistrationName"])
        if app_data["IsHtmlParsing"] == "true":
            url = find_latest_file_url(url, app_data["InstallationType"])
        response = http.get(url, stream=True)

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception:
        raise