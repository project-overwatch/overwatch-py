from sanic import Sanic
from sanic.response import json
import psutil
import arrow

app = Sanic()

# This endpoint returns the current server and UTC time.
@app.route('/timestamp')
async def getServerTimestamp(request):
    payload = {}
    payload['utc'] = arrow.utcnow().format('DD-MMM-YYYY HH:mm:SS ZZ')
    payload['local'] = arrow.now().format('DD-MMM-YYYY HH:mm:SS ZZ')
    payload['unix'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns current CPU times, along with a timestamp.
@app.route('/cpu/times')
async def getCpuTimes(request):
    payload = psutil.cpu_times()._asdict()
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns the current system-wide CPU utilization as a percentage.
@app.route('/cpu/usage')
async def getCpuUsage(request):
    payload = {}
    payload['usage'] = psutil.cpu_percent(interval=1)
    payload['cpus'] = psutil.cpu_percent(interval=1, percpu=True)
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns per-CPU times.
@app.route('/cpus/times')
async def getCpusTimes(request):
    payload = {}
    cpus_times = psutil.cpu_times_percent(interval=1, percpu=True)
    data = [item._asdict() for item in cpus_times]
    payload['cpus'] = data
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns CPU stats.
@app.route('/cpu/stats')
async def getCpuStats(request):
    payload = psutil.cpu_stats()._asdict()
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns frequency metrics for all CPUs, as well as per-CPU.
@app.route('/cpu/freq')
async def getCpuFreq(request):
    payload = psutil.cpu_freq()._asdict()
    all_cpus_freq = psutil.cpu_freq(percpu=True)
    payload['cpus'] = [cpu._asdict() for cpu in all_cpus_freq]
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint exposes system memory usage.
@app.route('/memory/usage')
async def getMemoryUsage(request):
    payload = psutil.virtual_memory()._asdict()
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint exposes swap memory usage.
@app.route('/memory/swap')
async def getSwapMemoryUsage(request):
    payload = psutil.swap_memory()._asdict()
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns all mounted disk partitions.
@app.route('/disks/partitions')
async def getDiskPartitions(request):
    payload = {}
    partitions = psutil.disk_partitions()
    payload['partitions'] = [partition._asdict() for partition in partitions]
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint exposes disk usage for a given mountpoint.
@app.route('/disks/usage')
async def getDiskUsage(request):
    payload = {}
    path = request.args['mountpoint']
    print(path)
    usage = psutil.disk_usage(path[0])
    payload['usage'] = usage._asdict()
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)

# This endpoint returns disk IO metrics.
@app.route('/disks/io')
async def getDiskIOCounters(request):
    payload = psutil.disk_io_counters()._asdict()
    disks_io = psutil.disk_io_counters(perdisk=True)
    disks = []
    for key, value in disks_io.items():
        disk = {}
        disk['name'] = key
        disk['io'] = value._asdict()
        disks.append(disk)
    payload['disks'] = disks
    payload['timestamp'] = arrow.now().timestamp
    return json(payload)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)