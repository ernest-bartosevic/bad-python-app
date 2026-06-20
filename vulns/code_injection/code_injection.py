from flask import render_template


def code_injection_page(request, app):
    expression = request.args.get('expr', '')
    result = None

    if expression:
        result = eval(expression)

    return render_template('code_injection.html', expression=expression, result=result)
