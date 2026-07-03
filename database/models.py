from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Problem(db.Model):

    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)

    problem_id = db.Column(db.String(30), unique=True)

    job_instance_id = db.Column(db.String(30))

    client_code = db.Column(db.String(20))

    client_name = db.Column(db.String(100))

    property_code = db.Column(db.String(20))

    property_name = db.Column(db.String(200))

    job_name = db.Column(db.String(200))

    step_name = db.Column(db.String(200))

    owner = db.Column(db.String(100))

    system_mode = db.Column(db.String(50))

    creation_date = db.Column(db.String(40))

    closed_date = db.Column(db.String(40))

    duration = db.Column(db.String(20))

    error_code = db.Column(db.String(50))

    node = db.Column(db.String(200))

    problem_description = db.Column(db.Text)