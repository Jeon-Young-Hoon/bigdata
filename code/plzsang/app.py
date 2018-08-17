from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/p404')
def p404():
    return render_template('404.html')


@app.route('/project_one')
def project_one():
    return render_template('project_one.html')


@app.route('/project_two')
def project_two():
    return render_template('project_two.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/project_details')
def project_details():
    return render_template('project_details.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')



if __name__ == '__main__':
    app.run()
