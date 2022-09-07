"""Launch UI."""
import os

import docker
import webbrowser

if __name__ == '__main__':

    client = docker.from_env()
    result = client.containers.run(
        'therealspring/inspring:latest',
        command='docker_command.py',
        tty=True,
        remove=True,
        volumes=[f'{os.path.dirname(os.path.realpath(__file__))}:/usr/local/workspace'])
    print(result)

    #result = webbrowser.open("http://localhost:7070")
    #print(result)
