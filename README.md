<div style="text-align:center;">
    <img src="snitch.png" width="150" height="150"/>
    <h1>Seeker</h1>
</div>

# Seeker

Seeker is just another job board aggregator. Check multiple job boards for positions you might be interested in and organize them all in one convenient location.

## Setup

### Docker

The easiest way to get started is to clone this repo and run docker-compose:

```
git clone git@github.com:NathanWorkman/seeker.git
cd seeker/
docker-compose build
docker-compose up
```

### To run the spiders

Execute the individual spiders from inside the docker container

```shell
docker exec -it seeker_app scrapy crawl spidername
```

or run all the spiders at once:

```shell
docker exec -it seeker_app python crawl.py
```

Navigate to `0.0.0.0:8000` to view results.
