#=======
**TEST**
#=======
A simple python function accepts an Author return all Books of that author using SQlAlchemy

### **Server-side**
* [Python 3.5+](http://www.python.org): The language of choice.

# create virtual environment
    virtualenv -p python3 venv
    
# activate virtual environment 
    source venv/bin/activate
    
# install requirements
    pip3 install -r requirements/default.txt
    
# upgrade migration
    python manage.py db upgrade
    
# seed sample data for testing
    python manage.py seed
    
# make new migartion for changes in schema
    python manage.py db migrate
    

