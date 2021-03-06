"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright 

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    github = request.form.get('github')
    first = request.form.get('first')
    last = request.form.get('last')

    hackbright.make_new_student(first, last, github)

    return render_template("student_added.html",
                           github=github)


@app.route("/add_student")
def student_add_form():
    """Show form for adding a student."""

    return render_template("add_student.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")


