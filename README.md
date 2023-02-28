#### Create virtual environment:

Install virtualenv

```
pip install virtualenv
```

Go to you project directory, then

```
python -m virtualenv venv
```

Windows

```
venv\bin\activate
```

Linux/Unix

```
source venv\bin\activate
```

#### Install requirements:

```
pip install -r requirements.txt
```

#### Set environmet variables:

```
PORT=
DEBUG=
SECRET_KEY=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```

#### Run docker:

```
docker-compose up -d
```
