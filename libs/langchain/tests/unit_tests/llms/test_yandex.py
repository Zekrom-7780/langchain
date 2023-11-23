import pytest
from langchain.llms import YandexGPT


@pytest.fixture
def valid_config():
    return {
        "iam_token": "VALID_IAM_TOKEN",
        "api_key": "VALID_API_KEY",
        "model_name": "general",
    }


@pytest.fixture
def invalid_config():
    return {
        "iam_token": "",
        "api_key": "",
        "model_name": "general",
    }


def test_valid_configuration(valid_config):
    yandex_gpt = YandexGPT(**valid_config)
    assert yandex_gpt.iam_token.get_secret_value() == "VALID_IAM_TOKEN"
    assert yandex_gpt.api_key.get_secret_value() == "VALID_API_KEY"


def test_invalid_configuration_raises_error(invalid_config):
    with pytest.raises(ValueError):
        YandexGPT(**invalid_config)