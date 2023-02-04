from tethys_sdk.base import TethysAppBase
from tethys_sdk.app_settings import CustomSimpleSetting,CustomSecretSetting,CustomJSONSetting


class TestAppStoreAquaveo(TethysAppBase):
    """
    Tethys app class for Test App Store Aquaveo.
    """

    name = 'Test App Store Aquaveo'
    description = ''
    package = 'test_app_store_aquaveo'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test-app-store-aquaveo'
    color = '#2d3436'
    tags = ''
    enable_feedback = False
    feedback_emails = []


    def custom_settings(self):
        custom_settings = (

            CustomSimpleSetting(
                name='Views_Names',
                type = CustomSimpleSetting.TYPE_STRING,
                description='Name of the region holding the views (e.g. La Plata Basin)',
                required=False,
                # default="HOLA"
            ),
            CustomJSONSetting(
                name='JSON_Test',
                description='This is JSON name',
                required=False,
                # default={"hola":"bebe"}
            ),
            CustomSecretSetting(
                name='Secret_Test',
                description='This is SECRET',
                required=True            
            ),
            CustomSecretSetting(
                name='Secret_Test2',
                description='This is SECRET',
                required=True
            ),
            CustomSecretSetting(
                name='Secret_Test3',
                description='This is SECRET',
                required=True
            ),
            CustomSecretSetting(
                name='Secret_Test4',
                description='This is SECRET',
                required=True
            ),

        )
        return custom_settings