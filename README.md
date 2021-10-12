# FlaskREST
this is a test rest api that using mongodb and flask

## Installation
first git clone

```bash
git clone https://github.com/amir2227/FlaskREST.git
```

make a virtualenv using below command

```bash
virtualenv env
```

activate venv


```bash
source env/bin/activate
```


Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install.

```bash
pip3 install -r requirements.txt
```

open app/__init__.py and enter your mongo configs like this

```python
app.config['MONGO_DBNAME'] = 'testdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/testdb'
```

now you can run the flask server

```bash
python3 run.py
```
## API End Points
**Show User**
----
  Returns json data about a single user.

* **URL**

  /get_one_user/<username>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `username=[string]`

----
  Returns json data about all user.

* **URL**

  /get_all_user

* **Method:**

  `GET`
  
