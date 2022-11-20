import qaseio
from qaseio.api import results_api
from qaseio.model.result_create import ResultCreate

from Configs.config import TestData

configuration = qaseio.Configuration(host=TestData.QASE_API)

configuration.api_key["TokenAuth"] = TestData.QASE_TOKEN


def update_test_results(
    run_id, case_id, status, comment="", project_code="", os_name=""
):
    # Enter a context with an instance of the API client
    with qaseio.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = results_api.ResultsApi(api_client)

        result_dict = dict(
            case_id=case_id,
            status=status,
            comment=comment,
        )
        if os_name:
            result_dict["param"] = {"OS": os_name}

        result_object = ResultCreate(**result_dict)

        try:
            api_response = api_instance.create_result(
                project_code, run_id, result_object
            )
            print(api_response)
        except qaseio.ApiException as e:
            print(f"Exception while trying to update result: {e}")
            print(result_dict)
