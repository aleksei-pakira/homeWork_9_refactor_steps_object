import dataclasses
from dataclasses import dataclass
import datetime
from enum import Enum


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    full_name: str


guest = User(first_name='Johann', last_name='Bach', user_email='Johann@Bach.com', full_name='Johann Bach')


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_date: datetime.date
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str


student = UserData(first_name='Johann', last_name='Bach', email='Johann@Bach.com', gender=Gender.male.value,
                   phone_number='4931031680', birth_date=datetime.date(1900, 1, 1), subject='Arts',
                   hobby=Hobby.music.value, file='organ.jpeg', address='Sophienstraße 41, 99817 Eisenach, Germany',
                   state='NCR', city='Delhi')
