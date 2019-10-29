import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'holiday_planning'
app.config["MONGO_URI"] = 'mongodb+srv://root:es1234@cluster0-dio8w.mongodb.net/holiday_planning?retryWrites=true&w=majority'
mongo = PyMongo(app)


# Function to display landing page
@app.route('/')
def index():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())
    

# Function to fetch all our data in mongodb pass it back to tasks.html
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", 
                            tasks=mongo.db.tasks.find())
    

# Function to fetch all our category in mongodb and pass it back to addTask.html <select> 
@app.route('/add_task')
def add_task():
    return render_template('addTask.html', 
                            category=mongo.db.category.find())
    
 
# Function will post new data to mondodb when click on the submit button in addTask.html. We convert the form to dictionary so can be understood by mon    
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
    


# CATEGORY

# Function to fetch all our data in mongodb pass it back to category.html
@app.route('/get_category')
def get_category():
    return render_template("category.html", 
                            category=mongo.db.category.find())
    
    
# Function to fetch all our category in mongodb and pass it back to addCategory.html <select> 
@app.route('/add_category')
def add_category():
    return render_template('addCategory.html')     

    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)