from selene import browser, be, command, have
from homeWork_9_refactor_steps_object.data.users import User


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
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.date_month_select = browser.element('.react-datepicker__month-select')
        self.date_year_select = browser.element('.react-datepicker__year-select')
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

    def fill_user_email(self, value):
        self.user_email.type(value)

    def registration(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_user_email(user.user_email)
        return self

    def practice_form_user_data(self, telephone_number, subject_input, current_address, select_state, select_city):
        self.choose_gender.perform(command.js.click).should(be.selected)
        self.choose_hobbies.perform(command.js.click).should(be.selected)
        self.telephone_number.type(telephone_number)
        self.subject_input.type(subject_input)
        self.select_hobbies_dropdown.click()
        self.current_address.type(current_address)          #street
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.select_state.element_by(have.exact_text(select_state)).click()
        self.city.click()
        self.select_city.element_by(have.exact_text(select_city)).click()

    def date_of_birth_calendar(self, year, month, day):
        self.date_of_birth.click()
        self.date_month_select .type(month)
        self.date_year_select.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def submit_form(self):
        self.submit_button.click()

    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                                    address, state_and_city):
        self.table.even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_and_city,
            )
        )
