from homeWork_9_refactor_steps_object.model.pages.steps_object_registration_form import UserRegistrationPage
from homeWork_9_refactor_steps_object import resources
from selene.support.shared import browser
from selene import browser
from homeWork_9_refactor_steps_object.data import users


def test_registration_form():
    registration_page = UserRegistrationPage()
    registration_page.open()

    registration_page.registration(users.guest)

    registration_page.practice_form_user_data('4931031680', 'art', 'Sophienstraße 41, 99817 Eisenach, Germany', 'NCR', 'Delhi')

    browser.element('#uploadPicture').set_value(resources.image_file_path('organ.jpeg'))

    registration_page.date_of_birth_calendar('1900', 'January', '01')

    registration_page.submit_form()

#    registration_page.should_have_data(users.guest)

    registration_page.should_registered_user_with('Johann Bach', 'Johann@Bach.com', 'Male', '4931031680',
                                                  '01 January,1900', 'Arts', 'Music', 'organ.jpeg',
                                                  'Sophienstraße 41, 99817 Eisenach, Germany', 'NCR Delhi')




