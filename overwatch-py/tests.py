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

def test_cpu_stats_endpoint():
    request, response = app.test_client.get('/cpu/stats')
    data = json.loads(response.text)
    assert response.status == 200
    if 'ctx_switches' in data:
        assert True
    else:
        assert False, "Context switches numbers are missing."
    if 'interrupts' in data:
        assert True
    else:
        assert False, "Interrupt numbers are missing."
    if 'soft_interrupts' in data:
        assert True
    else:
        assert False, "Soft interrupt numbers are missing."
    if "syscalls" in data:
        assert True
    else:
        assert False, "Syscall metrics are missing."
    if "timestamp" in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."
'''
def test_cpu_freq_endpoint():
    request, response = app.test_client.get('/cpu/freq')
    data = json.loads(response.text)
    print(data)
    assert response.status == 200
    if 'cpus' in data:
        assert True
    else:
        assert False, "CPU-specific frequency metrics are missing."
    if 'current' in data:
        assert True
    else:
        assert False, "Current CPU frequency is missing."
    if 'min' in data:
        assert True
    else:
        assert False, "Minimum CPU frequency is missing."
    if 'max' in data:
        assert True
    else:
        assert False, "Maximum CPU frequency is missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."
'''

def test_memory_usage_endpoint():
    request, response = app.test_client.get('/memory/usage')
    data = json.loads(response.text)
    assert response.status == 200
    if 'total' in data:
        assert True
    else:
        assert False, "Total physical memory numbers are missing."
    if 'available' in data:
        assert True
    else:
        assert False, "Available memory numbers are missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."

def test_swap_memory_usage_endpoint():
    request, response = app.test_client.get('/memory/swap')
    data = json.loads(response.text)
    assert response.status == 200
    if 'total' in data:
        assert True
    else:
        assert False, "Total swap memory numbers are missing."
    if 'used' in data:
        assert True
    else:
        assert False, "Used swap memory numbers are missing."
    if 'free' in data:
        assert True
    else:
        assert False, "Free swap memory numbers are missing."
    if 'percent' in data:
        assert True
    else:
        assert False, "Swap memory usage percentage numbers are missing."
    if 'sin' in data:
        assert True
    else:
        assert False, "Swapped in byte numbers are missing."
    if 'sout' in data:
        assert True
    else:
        assert False, "Swapped out byte numbers are missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."

def test_disk_partitions_endpoint():
    request, response = app.test_client.get('/disks/partitions')
    data = json.loads(response.text)
    assert response.status == 200
    if 'partitions' in data:
        assert True
    else:
        assert False, "Disk partitions info is missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."

def test_disk_usage_endpoint():
    request, response = app.test_client.get('/disks/usage?mountpoint=/')
    data = json.loads(response.text)
    assert response.status == 200
    if 'usage' in data:
        assert True
    else:
        assert False, "Disk usage data is missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."

def test_disk_io_endpoint():
    request, response = app.test_client.get('/disks/io')
    data = json.loads(response.text)
    assert response.status == 200
    if 'read_count' in data:
        assert True
    else:
        assert False, "Disk read counts are missing."
    if 'write_count' in data:
        assert True
    else:
        assert False, "Disk write counts are missing."
    if 'read_bytes' in data:
        assert True
    else:
        assert False, "Disk read byte counts are missing."
    if 'write_bytes' in data:
        assert True
    else:
        assert False, "Disk write byte counts are missing."
    if 'read_time' in data:
        assert True
    else:
        assert False, "Disk read times are missing."
    if 'write_time' in data:
        assert True
    else:
        assert False, "Disk write times are missing."
    if 'disks' in data:
        assert True
    else:
        assert False, "Disk-specific IO metrics are missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."

def test_network_io_endpoint():
    request, response = app.test_client.get('/network/io')
    data = json.loads(response.text)
    assert response.status == 200
    if 'bytes_sent' in data:
        assert True
    else:
        assert False, "Sent byte numbers are missing."
    if 'bytes_recv' in data:
        assert True
    else:
        assert False, "Received byte numbers are missing."
    if 'packets_sent' in data:
        assert True
    else:
        assert False, "Sent packet numbers are missing."
    if 'packets_recv' in data:
        assert True
    else:
        assert False, "Received packet numbers are missing."
    if 'errin' in data:
        assert True
    else:
        assert False, "Receiving error numbers are missing."
    if 'errout' in data:
        assert True
    else:
        assert False, "Sending error numbers are missing."
    if 'dropin' in data:
        assert True
    else:
        assert False, "Dropped incoming packet numbers are missing."
    if 'dropout' in data:
        assert True
    else:
        assert False, "Dropped outgoing packet numbers are missing."
    if 'nics' in data:
        assert True
    else:
        assert False, "NIC-specific IO metrics are missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."    

def test_system_boot_time_endpoint():
    request, response = app.test_client.get('/system/boot-time')
    data = json.loads(response.text)
    assert response.status == 200
    if 'boot_timestamp' in data:
        assert True
    else:
        assert False, "The system's boot timestamp is missing."
    if 'boot_date' in data:
        assert True
    else:
        assert False, "The system's boot date is missing."
    if 'timestamp' in data:
        assert True
    else:
        assert False, "The UNIX timestamp is missing."