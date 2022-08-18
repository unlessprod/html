import fastly
from fastly.api import pop_api
from pprint import pprint
configuration = fastly.Configuration()
configuration.api_token = 'FASTLY_API_TOKEN'
with fastly.ApiClient(configuration) as api_client:
    api_instance = pop_api.PopApi(api_client)
    
    try:
        api_response = api_instance.list_pops()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PopApi->list_pops: %s\n" % e)
