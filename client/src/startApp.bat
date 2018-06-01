cd %~dp0 %*
start chrome http://localhost:8080 %*
python server.py %*
exit %*