import pytest

from wikipedia_python import wikipedia

from .conftest import mock_requests_get

@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("wikipedia_python.wikipedia.random_page")

def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]

