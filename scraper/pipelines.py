# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from django.utils.text import slugify
from scrapy.exceptions import DropItem
from w3lib.html import remove_tags

from seeker.job.models import Job, Board, Company


class JobsPipeline(object):

    def process_item(self, item, spider):
        item['board'] = self.get_or_create_board(item['job_board'], item['board_url'])
        item['title'] = item['title']
        item['company'] = self.get_or_create_company(item['company'], item['email'])
        item['body'] = "\n".join(item['body'])  # extract() will return a list, which you need to concatenate to restore the original html
        item['pub_date'] = item['pub_date']
        item['salary'] = item['salary']
        item['location'] = self.clean_text(item['location'])

        """
        There's not a great way to find duplicate job postings so we pair
        job title with the published date to determine if a job warrants
        a new entry.
        """
        if not Job.objects.filter(title=item['title'], pub_date=item['pub_date']):
            item.save()
        else:
            raise DropItem('Job already exists.')
        """
        For every job that we create, delete the oldest job
        """
        # TODO: possibly remove this and just keep a large index of
        # job = Job.objects.all().last()
        # job.delete()

        return item

    def get_or_create_board(self, title, url):
        slug = slugify(title)
        try:
            return Board.objects.get(slug=slug)
        except Board.DoesNotExist:
            return Board.objects.create(title=title, slug=slug, url=url)

    def get_or_create_company(self, title, email):

        # Clean greenhouse company name
        if 'at' in title:
            cleantitle = title.replace("at", "")
            title = cleantitle
        
        slug = slugify(title)
        try:
            email = email[0].lower()
        except IndexError:
            email = ''
        try:
            return Company.objects.get(slug=slug)
        except Company.DoesNotExist:
            return Company.objects.create(title=title, slug=slug, email=email)

    def clean_text(self, text):
        output = remove_tags(text)
        return output
