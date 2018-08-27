from flask import Flask,render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80))
    name = db.Column(db.String(80))
    content = db.Column(db.String(80))
    source = db.Column(db.String(80))

    def __repr__(self):
        return '<Text %r>' % self.name

admin.add_view(TestModelView(data, db.session))


def load_data():
    import pandas as pd
    df = pd.read_csv('final.csv')
    for i in range(len(df)):
        id, date, name, content, source = df.iloc[i]
        me = data(id=int(id),date=date,name=name,content=content,source=source)
        db.session.add(me)

        if i % 5000 == 0:
            print(i)
    db.session.commit()
    print('finish')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/project_one')
def project_one():
    return render_template('project_one.html')


@app.route('/project_two')
def project_two():
    return render_template('project_two.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/teacher_details')
def teacher_details():
    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure()
    fig.sizing_mode = 'scale_width'
    fig.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'teacher_details.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)


@app.route('/project_details')
def project_details():
    return render_template('project_details.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run()
