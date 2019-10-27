  
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'holiday_planning'
app.config["MONGO_URI"] = 'mongodb+srv://root:es1234@cluster0-dio8w.mongodb.net/holiday_planning?retryWrites=true&w=majority'
mongo = PyMongo(app)


# this function fetch all our data in mongodb pass it back to tasks.html
@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())
    

# this function fetch all our category in mongodb and pass it back to addTask.htmk <select> 
@app.route('/add_task')
def add_task():
    return render_template('addtask.html', category=mongo.db.category.find())
    
 
# this function will post new data to mondodb when click on the submit button in addTask.html. We convert the form to dictionary so can be understood by mongo.    
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)