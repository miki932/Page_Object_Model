import requests
import json

# Set up your Qase API credentials
api_token = "YOUR_API_TOKEN"
project_code = "YOUR_PROJECT_CODE"

# Define the base URL for Qase API
base_url = "https://api.qase.io/v1"


def create_test_run(title, description):
    """Create a test run"""
    url = f"{base_url}/run/{project_code}"
    headers = {"Content-Type": "application/json", "Token": api_token}
    data = {"title": title, "description": description}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        test_run_id = response.json()["result"]["id"]
        return test_run_id
    else:
        raise Exception("Failed to create test run")


def add_test_case_result(test_run_id, case_id, status):
    """Add a test case result to the test run"""
    url = f"{base_url}/run/{project_code}/{test_run_id}/test-case/{case_id}"
    headers = {"Content-Type": "application/json", "Token": api_token}
    data = {"status": status}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise Exception("Failed to add test case result")
