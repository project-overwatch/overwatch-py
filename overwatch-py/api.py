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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)