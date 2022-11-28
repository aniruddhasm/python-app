from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', class_name="navbar-inverse", page_name="Home")

@app.route("/<string:page_name>")
def page(page_name):
    tmp = page_name.split('.')
    name = tmp[0].capitalize()
    return render_template(page_name, class_name="navbar-default", page_name=name)


def write_to_file(data):
    with open('database.txt', mode='a')  as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a')  as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            print('Something went wrong')
    else:
        print('Something is really wrong')


@app.route("/blog")
def blog():
    return "this is blog from python"
