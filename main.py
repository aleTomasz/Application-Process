from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city = request.args.get('city')

    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_cities(city)
    else:
        mentor_details = data_manager.get_mentors()


    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details, cities=data_manager.get_unique_cities(), selected_city=city)
@app.route('/applicants_phone')
def applicants_phone():
    applicant_first_name = request.args.get("first_name")

    if applicant_first_name:
        applicants_details = data_manager.get_applicants_data_by_name(applicant_first_name)
    else:
        applicants_details = None
    app.logger.info(applicant_first_name)
    app.logger.info(applicants_details)
    return render_template('applicant_phone.html', applicants=applicants_details)

if __name__ == '__main__':
    app.run(debug=True)
