<div style="text-align:center;">
    <img src="snitch.png" width="50" height="50"/>
</div>

# Seeker - [WIP]

Seeker is a job board aggregator. Check multiple job boards for positions you might be interested in and organize them all in one convenient location.

*This project is a WIP. If you find a bug or would like a new spider/feature added please open a pull request.*

## :gear:  Setup

#### Docker

The easiest way to get started is to clone this repo and run docker-compose:

```
git clone git@github.com:NathanWorkman/seeker.git
cd seeker/
docker-compose build
docker-compose up
```

#### To run the spiders

Execute the individual spiders from inside the docker container

```shell
docker exec -it seeker_app scrapy crawl spidername
```

or run all the spiders at once:

```shell
docker exec -it seeker_app python crawl.py
```

Navigate to `0.0.0.0:8000` to view results.


## :computer:  Job Boards

* [Django Gigs](https://djangogigs.com)
* [Greenhouse](https://greenhouse.io)
* [Indeed](https://indeed.com)
* [Lever](https://lever.co)
* [Python.org](https://www.python.org)
* [Recruiter Box](https://recruiterbox.com)
* [Remote Python](https://www.remotepython.com)
* [Stackoverflow Jobs](https://stackoverflow.com/)
* [Workable](https://workable.com)

 