from flask import render_template


def sql_injection_orders_page(request, app):
    user_id = request.args.get('user_id', '')
    orders = []

    if user_id:
        sql = f"SELECT * FROM orders WHERE user_id = {user_id}"
        db_result = app.db_helper.execute_read(sql)
        orders = list(
            map(
                lambda o: {'id': o[0], 'user_id': o[1], 'total': o[2]},
                db_result
            )
        )

    return render_template('sql_injection/orders.html', orders=orders, user_id=user_id)
