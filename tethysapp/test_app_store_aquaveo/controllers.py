from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button

from .app import TestAppStoreAquaveo as app
import json

@controller
def home(request):
    """
    Controller for the app home page.
    """

    normal_boy = app.get_custom_setting('Views_Names')
    json_boy = app.get_custom_setting('JSON_Test')

    secret_boy = app.get_custom_setting('Secret_Test')
    secret_boy1 = app.get_custom_setting('Secret_Test2')
    secret_boy2 = app.get_custom_setting('Secret_Test3')
    secret_boy3 = app.get_custom_setting('Secret_Test4')

    # json_dict =  json.loads(json_boy)

    # print(json_boy)
    print(normal_boy)
    print(json_boy)
    print(secret_boy)
    print(secret_boy1)
    print(secret_boy2)
    print(secret_boy3)

    save_button = Button(
        display_text='',
        name='save-button',
        icon='save',
        style='success',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='pen',
        style='warning',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='trash',
        style='danger',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-bs-toggle':'tooltip',
            'data-bs-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button,
        'normal_setting':normal_boy,
        'json_setting':json_boy,
        'secret1_setting':secret_boy,
        'secret2_setting':secret_boy1,
        'secret3_setting':secret_boy2,
        'secret4_setting':secret_boy3,
    }

    return render(request, 'test_app_store_aquaveo/home.html', context)