from flask import Flask, render_template

app = Flask(__name__)


sample_problem = {
    "problem_id":1802408,
    "client":"Hilton",
    "property":"DoubleTree Jacksonville Airport",
    "property_code":"JAXAR",
    "job_name":"NGI CDP Deferred Delivery Job",
    "job_instance":"446415369",
    "owner":"Ramesh Choudhary",
    "error_code":"UNEXPECTED_ERROR",
    "description":"Error processing CP Recommendation : Connection pool shut down"
}


@app.route("/")
def home():
    return render_template(
        "problem.html",
        problem=sample_problem
    )


if __name__=="__main__":
    app.run(debug=True)