import os

process1 = os.system("py -m pytest --headless --browser=edge --html=reportedge.html --maximize -n=4 ")
process2 = os.system("py -m pytest --headless --html=reportchrome.html --maximize -n=4 ")
