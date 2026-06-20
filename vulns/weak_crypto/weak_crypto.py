import hashlib
from flask import render_template


def weak_crypto_page(request, app):
    password = request.args.get('password', '')
    hashed = None

    if password:
        hashed = hashlib.md5(password.encode()).hexdigest()

    return render_template('weak_crypto.html', password=password, hashed=hashed)
