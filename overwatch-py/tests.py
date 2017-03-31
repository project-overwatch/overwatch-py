from api import app
import json


def test_timestamp_endpoint():
    request, response = app.test_client.get('/timestamp')
    data = json.loads(response.text)
    print(data)
    assert response.status == 200
    if 'utc' in data:
        assert True
    else:
        assert False, "The UTC timestamp is missing."
    if 'local' in data:
        assert True
    else:
        assert False, "The local timestamp is missing."
    if 'unix' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."
    