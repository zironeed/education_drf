from rest_framework import validators

ACCESS_LINK = 'youtube'


def validator_url(value):
    http_link = 'http'

    if http_link in value.split('s'):

        if ACCESS_LINK not in value.split('.'):
            raise validators.ValidationError('Используйте видео с youtube.com')
