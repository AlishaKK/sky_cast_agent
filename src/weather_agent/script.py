import subprocess

def run():
    subprocess.run(["chainlit" , "run" ,".//src//weather_agent//main.py" ,"-w"])