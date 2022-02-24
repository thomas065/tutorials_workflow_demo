from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial
from django.urls import reverse
import pytest

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"

@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk

@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True