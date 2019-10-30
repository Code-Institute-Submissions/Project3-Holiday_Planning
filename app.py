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
    

# T1 - Fetch data in mongodb pass it back to tasks.html
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", 
                            tasks=mongo.db.tasks.find())

    

# T2 & T3 - After add_task, must follow by insert_task
@app.route('/add_task')
def add_task():
    return render_template('addTask.html', 
                            category=mongo.db.category.find())
    
 
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
 
    

# T4 & T5 - After edit_task, must follow by update_task
@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_category =  mongo.db.category.find()
    return render_template('editTask.html', task=the_task,
                           category=all_category)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'category_name':request.form.get('category_name'),
        'task_name':request.form.get('task_name'),
        'task_description': request.form.get('task_description'),
        'person_in-charge': request.form.get('person_in-charge'),
        'website': request.form.get('website'),
        'due_date': request.form.get('due_date'),
        'is_urgent':request.form.get('is_urgent')
    })
    return redirect(url_for('get_tasks'))


# T6 - Delete task from the get_tasks page
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    return redirect(url_for('get_tasks'))


    


# CATEGORY

# C1 - Function to fetch all our data in mongodb pass it back to category.html
@app.route('/get_category')
def get_category():
    return render_template("category.html", 
                            category=mongo.db.category.find())
                            
   
    
# C2 & C3 - After add_category, must follow by insert_category   
@app.route('/add_category')
def add_category():
    return render_template('addCategory.html')   


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.category.insert_one(category_doc)
    return redirect(url_for('get_category'))
    
    
    
# C4 & C5 - After edit_category, must follow by update_category
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editCategory.html',
    category=mongo.db.category.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.category.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_category'))
    
    
    
# C6 - Delete category from the Manage Category page
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.category.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_category'))
    
    
    
# Boiler plate - must include at the end of app.py    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)