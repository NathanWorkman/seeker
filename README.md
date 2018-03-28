# :sunglasses: seeker [WIP]

Another job board aggregator. This is very much a work in progress and documentation is still incomplete. 

Right now the search terms are hard coded to remote django and python positions.

To change the search terms edit the query inside each spider.

Some quick setup instructions:

I would recommend installing [virtualenv](https://virtualenv.readthedocs.io/).

### To run the project
```
git clone git@github.com:NathanWorkman/seeker.git
cd seeker/
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
cd seeker/
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

### To run the spiders
From the root directory of the `seeker` project `cd` to seeker

```
cd seeker
```
and then run the following to run the individual spiders, replacing `spidername` with the spider you wish to run.

```
scrapy crawl spidername
```

Currently only the StackOverflow spider is working, others to come soon. 

```
scrapy crawl stackoverflow
```


Navigate to the django admin to view your results.