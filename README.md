<div style="text-align:center;">
    <img src="snitch.png" width="150" height="150"/>
    <h1>Seeker</h1>
</div>

[![Build Status](https://travis-ci.org/NathanWorkman/seeker.svg?branch=master)](https://travis-ci.org/NathanWorkman/seeker)

## What is Seeker?
Seeker is just another job board aggregator. Check multiple job boards for positions you might be interested in and organize them all in one convenient location.

## Setup

### Docker

Docker installation should be fairly straight forward.

```
git clone git@github.com:NathanWorkman/seeker.git
cd seeker/
docker-compose build
docker-compose up
```

### The hard(er) way:

You will need `yarn` and `virtualenv` installed on your machine.

Install Yarn
```
brew install yarn
```

Install virtualenv
```
pip install virtualenv
```

### To run the project
```
git clone git@github.com:NathanWorkman/seeker.git
cd seeker/
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
yarn
cd seeker/
python manage.py migrate
python manage.py createsuperuser
make build
make run
```

### To run the spiders
From the root directory of the `seeker` project `cd` to the seeker app directory.

```
cd seeker
```
and then run the following to run the individual spiders, replacing `spidername` with the spider you wish to run.

```
scrapy crawl spidername
```

or run all the spiders at once:

```
python crawl.py
```

Navigate to the django admin to view your results.

## TODO

### Boards 
- [x] DjangoGigs
- [ ] Indeed
- [ ] PythonOrg
- [ ] RemotePython
- [ ] Stack Overflow
- [ ] Workable
- [ ] Lever
- [ ] Recruiter Box
- [ ] Greenhouse
- [ ] TBD


## Made Possible By
- [Django](https://www.djangoproject.com/)
- [Scrapy](https://scrapy.org/)
- [jQuery](https://jquery.com/)
- Icons - [Devicon](http://konpa.github.io/devicon/)
- Admin Theme - [Django Suit](https://github.com/darklow/django-suit)
- NLP - [SpaCy](https://spacy.io/)
