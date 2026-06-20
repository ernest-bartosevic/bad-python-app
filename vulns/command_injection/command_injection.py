import subprocess
from flask import render_template


def command_injection_page(request, app):
    host = request.args.get('host', '')
    output = None

    if host:
        result = subprocess.run(
            f"ping -c 1 {host}",
            shell=True,
            capture_output=True,
            text=True
        )
        output = result.stdout + result.stderr

    return render_template('command_injection.html', host=host, output=output)
