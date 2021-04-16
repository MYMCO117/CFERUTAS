from Flask import flask, render_template, request, redirect, url_for

app = flask(_name_)

if _name_ == "_main_":
    app.run(port=3000, debug=True)