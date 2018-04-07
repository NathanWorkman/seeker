# :sunglasses: Seeker [WIP]

[![Build Status](https://travis-ci.org/NathanWorkman/seeker.svg?branch=master)](https://travis-ci.org/NathanWorkman/seeker)

## What is Seeker?
Seeker aims not to be a job board for everyone, but a job board for you.

Inevitably the time will come when you are on the hunt for a new job. Let Seeker do the leg work for you. Check multiple job boards for positions you might be interested in and organize them all in one convenient location.

Currently, the search terms are hard coded to remote django and remote python positions - you'll need to manually update these for now.

To change the search terms edit the query inside each spider.

## Setup

Some quick setup instructions

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
From the root directory of the `seeker` project `cd` to the seeker app directory.

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


## TODO

#### Future features.
- [x] Simple UI
- [ ] Enhanced UI
- [x] Pagination
- [ ] Breadcrumbs Navigation
- [ ] Settings Panel 
- [ ] Move all environmental variables to .env using PyEnv.
- [ ] Save/Favorite Job Postings
- [ ] Tag/Skill Views
- [ ] Full-Time, Part-Time, Contract
- [ ] Email Notifications - send daily, weekly, monthly email notifications of new job postings.
- [ ] Celery Beat - run spiders on a schedule.

#### Spiders
Want a spider not listed here? Feel free to open a pull request and add it to the list or implement the spider yourself.

- [x] [Stack Overflow](https://www.stackoverflow.com/jobs)
- [x] [Indeed](https://www.indeed.com)
- [ ] [Angel.co](https://angel.co/)
- [ ] [RemotePython](https://www.remotepython.com)
- [ ] [DjangoJobs](https://djangojobs.net/jobs/)
- [ ] [DjangoGigs](https://djangogigs.com)
- [ ] [Jobspresso](http://jobspresso.co)
- [ ] [We Work Remotely](https://weworkremotely.com/)
- [ ] [Python.org](https://www.python.org/jobs/)
- [ ] [Working Nomads](https://www.workingnomads.co/jobs)
- [ ] [Remote Work Hub](https://remoteworkhub.com)
- [ ] [Telecommunity](http://remotejobs.telecommunity.net/#s=1)
- [ ] [Remote Base](https://remotebase.io/)
- [ ] [WFH](https://www.wfh.io)
- [ ] [Remote Ok](https://remoteok.io)
- [ ] [Remotely Awesome Job](https://www.remotelyawesomejobs.com/remote-django-jobs)




