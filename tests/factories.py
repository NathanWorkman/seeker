import factory
from seeker.job.models import Board, Job
from seeker.company.models import Company


class CompanyFactory(factory.DjangoModelFactory):
    """Define Company Factory."""

    class Meta:
        model = Company


class BoardFactory(factory.DjangoModelFactory):
    """Define Board Factory"""

    class Meta:
        model = Board


class JobFactory(factory.DjangoModelFactory):
    """ Define Job Factory"""

    class Meta:
        model = Job

    board = factory.SubFactory(BoardFactory)
    company = factory.SubFactory(CompanyFactory)
