import hashlib
import time
from flask import render_template


def token_generator_page(request, app):
    username = request.args.get('username', '')
    token = None

    if username:
        raw = f"{username}{time.time()}"
        token = hashlib.md5(raw.encode()).hexdigest()

    return render_template('weak_crypto_token.html', username=username, token=token)
