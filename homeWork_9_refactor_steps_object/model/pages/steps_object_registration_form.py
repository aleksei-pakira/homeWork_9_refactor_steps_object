from selene import browser, be, command, have
from homeWork_9_refactor_steps_object.data.users import User
from homeWork_9_refactor_steps_object.data.users import UserData
from homeWork_9_refactor_steps_object.model.pages import table_registration_form
from homeWork_9_refactor_steps_object.model.pages.table_registration_form import DayOfBirth
from homeWork_9_refactor_steps_object.model.pages.table_registration_form import PracticeFormUserData
from homeWork_9_refactor_steps_object import resources


class UserRegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.choose_gender = browser.element('#gender-radio-1')
        self.telephone_number = browser.element('#userNumber')
        self.subject_input = browser.element('#subjectsInput')
        self.choose_hobbies = browser.element('#hobbies-checkbox-3')
        self.select_hobbies_dropdown = browser.element('[id="react-select-2-option-0"]')
        self.upload_picture = browser.element('#uploadPicture')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.date_month_select = browser.element('.react-datepicker__month-select')
        self.date_year_select = browser.element('.react-datepicker__year-select')
        self.date_day_select = browser.element(f'.react-datepicker__day--0{table_registration_form.birthday.day}:not('
                                               f'.react-datepicker__day--outside-month)')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.select_state = browser.all('[id^=react-select][id*=option]')
        self.city = browser.element('#city')
        self.select_city = browser.all('[id^=react-select][id*=option]')
        self.submit_button = browser.element('button#submit')
        self.table = browser.element('.table').all('td')

    @staticmethod
    def open():
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_current_email(self, value):
        self.user_email.type(value)

    def registration(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_current_email(user.user_email)
        return self

    def fill_current_telephone(self, value):
        self.telephone_number.type(value)

    def fill_current_subject(self, value):
        self.subject_input.type(value)

    def fill_current_address(self, value):
        self.current_address.type(value)

    def fill_current_state(self, value):
        self.select_state.element_by(have.exact_text(value)).click()

    def fill_current_city(self, value):
        self.select_city.element_by(have.exact_text(value)).click()

    def practice_form_user_data(self,
                                current_data: PracticeFormUserData):
        self.choose_gender.perform(command.js.click).should(be.selected)
        self.choose_hobbies.perform(command.js.click).should(be.selected)
        self.fill_current_telephone(current_data.telephone_number)
        self.fill_current_subject(current_data.subject_input)
        self.select_hobbies_dropdown.click()
        self.upload_picture.set_value(resources.image_file_path('organ.jpeg'))
        self.fill_current_address(current_data.current_address)
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.fill_current_state(current_data.select_state)
        self.city.click()
        self.fill_current_city(current_data.select_city)

    def fill_date_of_month_check(self, value):
        self.date_month_select.type(value)

    def fill_date_of_year_check(self, value):
        self.date_year_select.type(value)

    def fill_date_day_check(self, value):
        self.date_day_select(value)

    def date_of_birth_calendar(self, users_birthday: DayOfBirth):
        self.date_of_birth.click()
        self.fill_date_of_month_check(users_birthday.mouth)
        self.fill_date_of_year_check(users_birthday.year)
        self.date_day_select().click()

    def submit_form(self):
        self.submit_button.click()

    @staticmethod
    def should_have_registered(user: UserData):
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            user.birth_date.strftime('%d %B,%Y'),
            user.subject,
            user.hobby,
            user.file,
            user.address,
            f'{user.state} {user.city}'
        )
        )
