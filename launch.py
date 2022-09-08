"""Launch UI."""
import os

import docker
import webbrowser

if __name__ == '__main__':

    client = docker.from_env()
    result = client.containers.run(
        'therealspring/inspring:latest',
        command='app.py',
        tty=True,
        remove=True,
        ports={'5000/tcp': 5000},
        volumes=[f'{os.path.dirname(os.path.realpath(__file__))}:/usr/local/workspace'])
    print(result)

    # TODO: how does container shut down if main thread dies?
    # TODO: stream stdout somehow from container?
    # TODO: keep pinging container in webpage until it loads?

    #result = webbrowser.open("http://localhost:7070")
    #print(result)
