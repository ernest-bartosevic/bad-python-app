from flask import render_template

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_PASSWORD = "SuperSecretPassword123!"
STRIPE_API_KEY = "sk_live_abc123secretstripekey000000"


def hardcoded_secrets_page(request, app):
    return render_template('hardcoded_secrets.html')
