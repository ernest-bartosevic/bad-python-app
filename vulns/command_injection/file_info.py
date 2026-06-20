import subprocess
from flask import render_template


def file_info_page(request, app):
    filename = request.args.get('filename', '')
    output = None

    if filename:
        result = subprocess.run(
            f"file {filename}",
            shell=True,
            capture_output=True,
            text=True
        )
        output = result.stdout + result.stderr

    return render_template('command_injection_file.html', filename=filename, output=output)
