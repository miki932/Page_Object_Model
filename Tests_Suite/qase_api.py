# import os
#
# import qaseio
# import requests
# from datetime import datetime
# from dotenv import load_dotenv
# from qaseio.api import runs_api
# from qaseio.model.run_create import RunCreate
#
# # Load the environment variables from the .env file
# load_dotenv()
#
# # Get the values from the environment variables
# api_token = os.getenv("QASE_API_TOKEN")
# project_code = os.getenv("QASE_PROJECT_CODE")
#
# # Define the base URL for Qase API
# base_url = 'https://api.qase.io/v1'
#
# configuration = qaseio.Configuration(host=base_url)
# configuration.api_key['TokenAuth'] = api_token
#
#
# # Set up headers with the API token
# headers = {
#     "Content-Type": "application/json",
#     "Token": api_token
# }
#
#
# def create_test_run_1(title_prefix, description):
#     """Create a test run"""
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%d/%m/%Y_%H:%M")
#     title = f"{title_prefix} - {formatted_time}"
#
#     url = f"{base_url}/run/{project_code}"
#     data = {"title": title, "description": description}
#     response = requests.post(url, json=data, headers=headers)
#     response.raise_for_status()
#     test_run_id = response.json()["result"]["id"]
#     return test_run_id
#
#
# def create_qase_test_run_2(title: str, project_code: str = 'AZTC', custom_fields: dict = None, **kwargs):
#     """
#     Create a test run in Qase for the provided project with the title.
#     :param title: The title for the test run
#     :param project_code: The Qase project code string. e.g. 'AZTC'.
#     :param custom_fields: An optional dictionary that populates custom fields in the test run in Qase.
#     e.g. {
#             "3": "5.0.0-cb4e787",
#             "1": "https://autoetp2.jenkins.akamai.com/job/aztc-desktop-smoke-test/125/allure/",
#         }
#     :return: The Qase API result dict with 'status' key containing a boolean.
#     """
#
#     args = {
#         "title": title,
#         "is_autotest": True,
#     }
#     if custom_fields is not None:
#         args["custom_field"] = custom_fields
#     args.update({k: v for k, v in kwargs.items() if v})
#     with qaseio.ApiClient(configuration) as api_client:
#         api_instance = runs_api.RunsApi(api_client)
#
#         try:
#             api_response = api_instance.create_run(project_code, RunCreate(**args))
#             return api_response
#         except qaseio.ApiException as e:
#             print(f"Exception while trying to create a test run: {e}")
#
#
# def add_test_case_result(test_run_id, case_id, status):
#     """Add a test case result to the test run"""
#     url = f"{base_url}/run/{project_code}/{test_run_id}/test-case/{case_id}"
#     data = {"status": status}
#     response = requests.post(url, json=data, headers=headers)
#     response.raise_for_status()
#
#
# def complete_test_run_1(test_run_id):
#     """Complete the test run"""
#     url = f"{base_url}/run/{project_code}/{test_run_id}/complete"
#     response = requests.post(url, headers=headers)
#     response.raise_for_status()
#
#
# def complete_qase_test_run_2(run_id: int, project_code: str = 'POM'):
#     """
#     Completes a test run in Qase.
#     """
#
#     with qaseio.ApiClient(configuration) as api_client:
#         api_instance = runs_api.RunsApi(api_client)
#
#         try:
#             api_response = api_instance.complete_run(project_code, run_id)
#             return api_response
#         except qaseio.ApiException as e:
#             print(f"Exception while trying to complete a Qase run: {e}")
