from flask import render_template, url_for, request, redirect
from models import app, db, Project, datetime



@app.context_processor
def inject_projects():
    projects = Project.query.all()
    return dict(projects=projects)

@app.route('/')
def index():
    return render_template('index.html')


    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project<id>')
def detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project)

@app.route('/project/new', methods=['GET', 'POST'])
def project_form():
    if request.form:
        new_project = Project(title=request.form['title'],
                              date=request.form['date'],
                              desc=request.form['desc'],
                              skills=request.form['skills'],
                              github_link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('projectform.html')

@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get(id)
    if request.form:
        date_str = request.form['date']
        project.title = request.form['title']
        project.date = datetime.strptime(date_str, '%Y-%m')
        project.desc = request.form['desc']
        project.skills = request.form['skills']
        project.github_link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project)

@app.route('/project/<id>/delete')
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000,host='127.0.0.1')
    