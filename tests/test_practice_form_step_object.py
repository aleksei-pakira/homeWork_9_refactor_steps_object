from homeWork_9_refactor_steps_object.model.pages.steps_object_registration_form import UserRegistrationPage
from homeWork_9_refactor_steps_object.data import users
from homeWork_9_refactor_steps_object.model.pages import table_registration_form


def test_registration_form():
    registration_page = UserRegistrationPage()

    registration_page.open()

    registration_page.registration(users.guest)

    registration_page.practice_form_user_data(table_registration_form.current_data)

    registration_page.date_of_birth_calendar(table_registration_form.birthday)

    registration_page.submit_form()

    registration_page.should_have_registered(users.student)
