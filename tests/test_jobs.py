import pytest
from factories import BoardFactory, JobFactory, CompanyFactory


@pytest.mark.django_db
def test_board_model():
    """ Test customer model """
    # create customer model instance
    board = BoardFactory(title="Job Board Title")
    assert board.title == "Job Board Title"


# @pytest.mark.django_db
# def test_job_creation():
#     """ Test quote model """
#     # create customer and quote model instances
#     customer = CustomerFactory(name="Test Customer Name")
#     quote = QuoteFactory(customer=customer, price=100.00)

#     assert quote.customer == customer
#     asset quote.customer.name == "Test Customer Name"
#     assert quote.price == 100.00
