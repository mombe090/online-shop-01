# online-shop-01
Build e-commerce plateform for students

# Get started
## 1. Create and Activate virtuelenv
``sh
python3.12 -m venv venv
source venv/bin/activate # for lunix / mac
venv\Scripts\activate # for windows
``

## 2. Install dependancies
``sh
pip install -r requirements.txt
``

## 3. Create admin user
``sh
python manage.py createsuperuser
``

## 4. Run server
``sh
python manage.py runserver
``

Open http://localhost:8000 to your browser
