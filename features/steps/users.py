from behave import *
import requests

URL = "https://reqres.in/{req_call}"
global global_data


@given("I set the page number 2")
def step_impl(context):
    context.response = {"page": 2}


@when("I call api /api/users?page=2 , check status code 200")
def step_impl(context):
    req = requests.get(URL.format(req_call="api/users"), params=context.response)
    assert req.status_code == 200
    context.response = req


@then("I validate the output that should return 3 elements")
def step_impl(context):
    json_data = context.response.json()
    assert isinstance(json_data, dict) is True
    assert len(json_data["data"]) == 3
    global global_data
    global_data = json_data.copy()


@given("I will give an id from the last scenario, randomically")
def step_impl(context):
    global global_data
    global_data["data"]
    users_id = []
    for i in global_data["data"]:
        users_id.append(i["id"])

    context.response = users_id


@when("I call api /api/users/<scenario1> with random data, check status code 200")
def step_impl(context):
    random_id = context.response[0]
    req = requests.get(URL.format(req_call=f"api/users/{random_id}"))
    assert req.status_code == 200
    context.response = req


@then("I Validate the output and check all data structure")
def step_impl(context):
    print(context.response.json())
    data = context.response.json()
    assert data["data"]["id"] == 4


@given("I will pass a invalid id user")
def step_impl(context):
    context.response = {"user_id": 999_999_999}


@when("I call api /api/users/999999999")
def step_impl(context):
    req = requests.get(
        URL.format(req_call="api/users/{user_id}".format(**context.response))
    )
    context.response = req


@then("I validate if status code should be 404")
def step_impl(context):
    assert context.response.status_code == 404
