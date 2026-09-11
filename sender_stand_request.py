import requests
import configuration
import data


def post_create_users(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )


def post_create_kit(body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + auth_token
    }

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=body,
        headers=headers
    )