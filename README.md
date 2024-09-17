# online-shop-01
Build e-commerce plateform for students

# Get started
## 0. Clone project
```sh
git clone git@github.com:1000TechLeaders/online-shop-01.git
```
## 1. Create and Activate virtuelenv
```sh

python3.12 -m venv venv

source venv/bin/activate # for lunix / mac

venv\Scripts\activate # for windows

```

## 2. Install dependancies
```sh
pip install -r requirements.txt
```

### 2.1 Dev dependancies
```sh
pip install -r requirements-dev.txt
```

## 3. Create admin user
```sh
python manage.py createsuperuser
```

## 4. Run server
```sh
python manage.py runserver
```

Open http://localhost:8000 to your browser
