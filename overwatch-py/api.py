from sanic import Sanic
from sanic.response import json
import psutil
import arrow

app = Sanic()

@app.route('/timestamp')
async def getServerTimestamp(request):
    payload = {}
    payload['utc'] = arrow.utcnow().format('DD-MMM-YYYY HH:mm:SS ZZ')
    payload['local'] = arrow.now().format('DD-MMM-YYYY HH:mm:SS ZZ')
    payload['unix'] = arrow.now().timestamp
    return json(payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)