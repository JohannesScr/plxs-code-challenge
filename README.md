# Code Challenge

The following is all from the root directory of the server. If cloned from 
github the root directory would be `plxs-code-challenge`. 

## Initial set-up
The following script is idempotent, `setup.sh` and can be run the the terminal 
to setup the  
```bash
./setup.sh
```
next start the virtual environment for the server with,
```bash
source  ../venv/bin/activate
```
now that the virtual environment is up and running. 

## Test Server
To test the server,
```bash
pytest -vv --cov-report term-missing --cov=. tests/
```
all the  test should pass.

## Run  Server
To run the server, simply
```bash 
python server.py
```