# pycon-demo
Demo GraphQL server for my talk  @Pycon Nigeria 2018 Conference.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

# Prerequisites

So before you get started here are the things you might need:

- Python >= 3.6


# Installing
- Now that you have all the requirements setup, these are the installation steps:

```
Make a folder and Clone the repo:
mkdir Project && cd Project
git clone https://github.com/samie820/pycon-demo.git .
```
- Install the `requirements.txt` file:

```
pip install -r requirements.txt
```

- Migrate and then run the server:
```
python manage.py migrate
python manage.py runserver
```
# And  voilà!!!
