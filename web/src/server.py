from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from datetime import datetime
import mysql.connector as mysql
import os
from pyramid.response import Response
import json

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/home.html',[],request = req)

def cv(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/cv.html',[],request = req)

def about(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/about.html',[],request = req)

def avatar(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select avatar from Users;")
  records = cursor.fetchall()
  db.close()

  SOME_DATA_ARRAY = {"image_src": records[0][0]}
  response = Response(body = json.dumps(SOME_DATA_ARRAY))
  response.headers.update({'Access-Control-Allow-Origin':'*',})
  return response


def personal(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  SOME_DATA_ARRAY = {"first_name": records[0][0], "last_name": records[0][1], "email": records[0][2]}
  response = Response(body = json.dumps(SOME_DATA_ARRAY))
  response.headers.update({'Access-Control-Allow-Origin':'*',})
  return response


def education(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select school, degree, major, date from Users;")
  records = cursor.fetchall()
  db.close()

  SOME_DATA_ARRAY = {"school": records[0][0], "degree": records[0][1], "major": records[0][2], "date": records[0][3]}
  response = Response(body = json.dumps(SOME_DATA_ARRAY))
  response.headers.update({'Access-Control-Allow-Origin':'*',})
  return response


def project(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select title, description, link, Image_src,team from Users;")
  records = cursor.fetchall()
  db.close()

  SOME_DATA_ARRAY = {"title": records[0][0], "description": records[0][1], "link": records[0][2], "Image_src": records[0][3], "team": records[0][4]}
  response = Response(body = json.dumps(SOME_DATA_ARRAY))
  response.headers.update({'Access-Control-Allow-Origin':'*',})
  return response 
  
def welcome(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email, comment from Users;")
  records = cursor.fetchall()
  db.close()
  return render_to_response('templates/welcome.html', {'users': records}, request=req)

def pushtoserver(tempc):
    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()
    time_stamp = str(datetime.now())
    push1 = """INSERT INTO Users(
        first_name,last_name, email, comment, created_at)
        VALUES (%s, %s, %s, %s, %s)"""
    input1 = (tempc[0],tempc[1],tempc[2],tempc[3],time_stamp)
    cursor.execute(push1,input1)
    db.commit()

def add_user(req):
    personal=req.json_body
    temp = [str(personal['first']),str(personal['last']),str(personal['em']),str(personal['com'])]
    pushtoserver(temp)


''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('welcome', '/welcome')
  config.add_view(welcome, route_name='welcome')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('cv', '/cv')
  config.add_view(cv, route_name='cv')

  config.add_route('about', '/about')
  config.add_view(about, route_name='about')

  config.add_route('avatar', '/avatar')  
  config.add_view(avatar, route_name='avatar',renderer = 'json')

  config.add_route('personal', '/personal')  
  config.add_view(personal, route_name='personal',renderer = 'json')

  config.add_route('education', '/education')  
  config.add_view(education, route_name='education',renderer = 'json')

  config.add_route('project', '/project')  
  config.add_view(project, route_name='project',renderer = 'json')

  config.add_route('add_user', '/add_user')
  config.add_view(add_user, route_name='add_user',renderer = 'json')

  
  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()