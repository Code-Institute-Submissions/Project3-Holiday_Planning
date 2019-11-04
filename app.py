import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'holiday_planning'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)



# T1 - Fetch data in mongodb pass it back to todos.html
@app.route('/')
def get_todos():
    critera= {}
    category = request.args.get('category')
    
    if category and category != 'All Category':
        critera['category_name'] = category
    else:
        category = 'All Category'
        
    todos=mongo.db.todos.find(critera)
    print(todos)
    return render_template("todos.html", 
                           todos=todos, category_name=category)

    

# T2 & T3 - After add_todo, must follow by insert_todo
@app.route('/add_todo')
def add_todo():
    return render_template('addTodo.html', 
                            category=mongo.db.category.find())
    
 
@app.route('/insert_todo', methods=['POST'])
def insert_todo():
    todos = mongo.db.todos
    todos.insert_one(request.form.to_dict())
    return redirect(url_for('get_todos'))
 
    

# T4 & T5 - After edit_todo, must follow by update_todo
@app.route('/edit_todo/<todo_id>')
def edit_todo(todo_id):
    the_todo =  mongo.db.todos.find_one({"_id": ObjectId(todo_id)})
    all_category =  mongo.db.category.find()
    return render_template('editTodo.html', todo=the_todo,
                           category=all_category)


@app.route('/update_todo/<todo_id>', methods=["POST"])
def update_todo(todo_id):
    todos = mongo.db.todos
    todos.update( {'_id': ObjectId(todo_id)},
    {
        'category_name':request.form.get('category_name'),
        'todo_title':request.form.get('todo_title'),
        'todo_description': request.form.get('todo_description'),
        'person_in-charge': request.form.get('person_in-charge'),
        'website': request.form.get('website'),
        'due_date': request.form.get('due_date'),
        'is_urgent':request.form.get('is_urgent')
    })
    return redirect(url_for('get_todos'))


# T6 - Delete todo from the get_todos page
@app.route('/delete_todo/<todo_id>')
def delete_todo(todo_id):
    mongo.db.todos.remove({'_id': ObjectId(todo_id)})
    return redirect(url_for('get_todos'))
    


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