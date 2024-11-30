from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Dhaka, Bangladesh',
    'salary': '55,000 BDT'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Chittagong, Bangladesh',
    'salary': '65,000 BDT'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Sylhet, Bangladesh'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': '$2,000'
  },
]

@app.route("/")
def home():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name='Horizon')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


