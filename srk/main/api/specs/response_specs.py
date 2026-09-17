from http import HTTPStatus

from requests import Response


class ResponseSpecs:
    @staticmethod
    def requests_ok():
        def confirm(response:Response):
            assert response.status_code == HTTPStatus.OK, response.text
        return confirm

    @staticmethod
    def requests_create():
        def confirm(response:Response):
            assert response.status_code == HTTPStatus.CREATED, response.text
        return confirm

    @staticmethod
    def requests_bad():
        def confirm(response:Response):
            assert response.status_code == HTTPStatus.BAD_REQUEST, response.text
        return confirm

    