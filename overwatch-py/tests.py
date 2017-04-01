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

def test_cpu_times_endpoint():
    request, response = app.test_client.get('/cpu/times')
    data = json.loads(response.text)
    print(data)
    assert response.status == 200
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."
    if 'idle' in data:
        assert True
    else:
        assert False, "Idle CPU times are missing."
    if 'nice' in data:
        assert True
    else:
        assert False, "Prioritized process times are missing."
    if 'system' in data:
        assert True
    else:
        assert False, "System CPU times are missing."
    if 'user' in data:
        assert True
    else:
        assert False, "User CPU times are missing."

def test_cpu_usage_endpoint():
    request, response = app.test_client.get('/cpu/usage')
    data = json.loads(response.text)
    print(data)
    assert response.status == 200
    if 'usage' in data:
        assert True
    else:
        assert False, "CPU usage stats are missing."
    if 'cpus' in data:
        assert True
    else:
        assert False, "CPU-specific usage stats are missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."

def test_cpus_times_endpoint():
    request, response = app.test_client.get('/cpus/times')
    data = json.loads(response.text)
    print(data)
    assert response.status == 200
    if 'cpus' in data:
        assert True
    else:
        assert False, "CPU-specific times are missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."