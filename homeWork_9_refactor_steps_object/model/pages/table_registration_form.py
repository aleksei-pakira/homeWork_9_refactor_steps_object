import dataclasses


@dataclasses.dataclass
class DayOfBirth:
    year: str
    mouth: str
    day: str


birthday = DayOfBirth(year='1900', mouth='January', day='01')


@dataclasses.dataclass
class PracticeFormUserData:
    telephone_number: str
    subject_input: str
    current_address: str
    select_state: str
    select_city: str


current_data = PracticeFormUserData(telephone_number='4931031680', subject_input='art',
                                    current_address='Sophienstraße 41, 99817 Eisenach, Germany', select_state='NCR',
                                    select_city='Delhi')
