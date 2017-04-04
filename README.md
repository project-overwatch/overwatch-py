[![Build Status](https://travis-ci.org/project-overwatch/overwatch-py.svg?branch=master)](https://travis-ci.org/project-overwatch/overwatch-py)
# overwatch
A RESTful API for exposing psutil. 

## Usage

1. Clone the repo:

`git clone https://github.com/project-overwatch/overwatch-py.git`

2. Install dependencies:

`pip install -r requirements.txt`

You can install them globally, or insinde a virtualenv - your call.

3. Make sure port 8000 is open in your server firewall, or in your cloud VM's security group.

4. Run the server:

`python overwatch-py/api.py`

A list of available routes and their payloads can be found in the code itself, in `api.py`. A Swagger spec is on the way.

If you'd like to run the test suite:
`pytest overwatch-py/tests.py`

## Contributions..

..are more than welcome. Please fork the code, hack to your heart's content and file a PR. Also, please make sure any new endpoints
you add are backed up by a test case, in `tests.py`.

If you find bugs/issues/better ways to do things, feel free to file an issue too! Hopefully I'd be able to work on it.

## License

[MIT License - Copyright (c) 2017 Rudraksh MK](https://github.com/project-overwatch/overwatch-py/blob/master/LICENSE)