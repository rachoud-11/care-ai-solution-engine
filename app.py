from flask import Flask, render_template
from config import Config
from database.models import db, Problem

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


@app.before_request
def create_database():

    db.create_all()

    if Problem.query.count() == 0:

        sample = Problem(

            problem_id="1802430",

            job_instance_id="446434719",

            client_code="Hilton",

            client_name="Hilton",

            property_code="LAXTM",

            property_name="Embassy Suites by Hilton Temecula Valley Wine Country",

            job_name="NGI Hilton FPLOS Decision Delivery Job",

            step_name="evaluateForceFullDecisionsStep",

            owner="N/A",

            system_mode="Decision Delivery Mode",

            creation_date="03-Jul-2026 15:51:14 PM",

            closed_date="N/A",

            duration="00:34:56",

            error_code="UNEXPECTED_ERROR",

            node="mn5pg3xappl104.ideasprod.int",

            problem_description="org.springframework.batch.core.JobExecutionException: Flow execution ended unexpectedly..."
        )

        db.session.add(sample)

        db.session.commit()


@app.route("/")
def problems():

    problems = Problem.query.all()

    return render_template(

        "problems.html",

        problems=problems

    )


@app.route("/problem/<problem_id>")
def problem_detail(problem_id):

    problem = Problem.query.filter_by(

        problem_id=problem_id

    ).first()

    return render_template(

        "problem_detail.html",

        problem=problem

    )


if __name__ == "__main__":
    app.run(debug=True)