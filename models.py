from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String(80), unique=True)
    date = db.Column('Date', db.Date)
    desc = db.Column('Description', db.String(500))
    skills = db.Column('Skills', db.String(80))
    github_link = db.Column('Github', db.String(120), unique=True)

    def __init__(self, title, date, desc, skills, github_link):
        self.title = title
        self.date = datetime.strptime(date, '%Y-%m').date()
        self.desc = desc
        self.skills = skills
        self.github_link = github_link
        
    def __repr__(self):
        return f'''<Project  (Title: {self.title} 
                    Date: {self.date}
                    Description: {self.desc}
                    Skills: {self.skills}
                    Github: {self.github_link})
    '''