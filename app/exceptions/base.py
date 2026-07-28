from http import HTTPStatus


class ApplicationException(Exception):
    """
    Base application exception.

    Every exception in the project
    should inherit from this class.
    """

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
    ) -> None:
        self.message = message
        self.code = code
        self.status_code = status_code

        super().__init__(message)
