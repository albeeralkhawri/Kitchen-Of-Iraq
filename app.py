import os
from flask import Flask, render_template, redirect, request, url_for, Response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from gridfs import GridFS

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'IraqDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)
files = GridFS(mongo.db)
@app.route('/')

# for home page
@app.route('/home')
def home():
    return render_template("home.html", login=mongo.db.IQ2019.find())

    
# for register form to To save data in mongodb
@app.route('/register', methods=['POST']) 
def register():
    print(request.form)
    data = dict(request.form)
    user_name = data['user_name']
    password = data['password']
    mongo.db.users.insert_one({"user_name": user_name, "password": password})
    return redirect(url_for('get_recipes'))
    
    
# for login form to join with mongodb data
@app.route('/login', methods=['POST'])
def login():
    data = dict(request.form)
    print(data)
    user_name = data['user_name']
    password = data['password']
    mongo_data = mongo.db.users.find_one({"user_name": user_name})
    print(mongo_data)
    return redirect(url_for('get_recipes'))
  
 # for add recipes  
@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipes.html',
                           Categories=mongo.db.OfIraqMDB.find())
   
# for insert recipe
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    if 'recipe_image' not in request.files:
        return "Error"
        
    # Extract the photo from the request
    image = request.files.get('recipe_image')
    
    # Save the photo in mongo
    files.put(
        image,
        content_type=image.content_type,
        filename=image.filename
    )
    
    # Save the recipe into the database with the filename
    recipe_data = (request.form.to_dict())
    recipe_data['recipe_image'] = image.filename
    recipes.insert_one(recipe_data)
    return redirect(url_for('get_recipes'))


#for get recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


# for search name of recipes
@app.route('/search', methods=['POST'])
def search():
    search_data = dict(request.form)
    recipe_name = search_data["search"]
    mongo_data = mongo.db.recipes.find({"recipe_name": recipe_name})
    return render_template("recipes.html", recipes=mongo_data)
 
    
# for edit recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_Categories =  mongo.db.OfIraqMDB.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           Categories=all_Categories)
  
    
#for update recipe                       
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    image = request.files.get('recipe_image')
    files.put(
        image,
        content_type=image.content_type,
        filename=image.filename
    )
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_image': image.filename,
        'is_Recommended':request.form.get('is_Recommended')
    })
    return redirect(url_for('get_recipes'))
    

@app.route('/images/<filename>')
def image(filename):
    image = files.get_last_version(filename=filename)
    return Response(image.read(), mimetype=image.content_type)
    
# for delete recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    

# categories
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.OfIraqMDB.find())
                           
                           
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.OfIraqMDB.find_one(
                           {'_id': ObjectId(category_id)}))
                           
                           
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.OfIraqMDB.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))
    
    
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.OfIraqMDB.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))
    
    
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.OfIraqMDB.insert_one(category_doc)
    return redirect(url_for('get_categories'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
             port=int(os.environ.get('PORT')),
             debug=True)