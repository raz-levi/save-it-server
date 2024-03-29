from injector import inject
from abc import ABC, abstractmethod
from common.interface.auto_mapper_interface import AutoMapperInterface
from services.authentication_service.client.api.sign_up.sign_up_request_api import EmailSignUpRequestApi
from services.authentication_service.client.api.sign_up.sign_up_response_api import EmailSignUpResponseApi
from services.authentication_service.core.processor.authentication_service_processor import AuthenticationServiceProcessorInterface
from services.authentication_service.core.models.sign_up.sign_up_request import EmailSignUpRequest
from services.authentication_service.client.api.checklivestatus.authentication_check_live_status_response_api import AuthenticationCheckLiveStatusResponseApi


class AuthenticationServiceControllerInterface(ABC):
    @abstractmethod
    def checklivestatus(self) -> AuthenticationCheckLiveStatusResponseApi:
        pass

    @abstractmethod
    def email_sign_up(self, email_sign_up_request_api: EmailSignUpRequestApi) -> EmailSignUpResponseApi:
        pass

    @abstractmethod
    def email_login(self, email_sign_up_request: EmailSignUpRequestApi) -> EmailSignUpResponseApi:
        pass


class AuthenticationServiceController(AuthenticationServiceControllerInterface):
    @inject
    def __init__(self, mapper: AutoMapperInterface, authentication_service_processor: AuthenticationServiceProcessorInterface):
        self._mapper = mapper
        self._authentication_service_processor = authentication_service_processor

    def checklivestatus(self) -> AuthenticationCheckLiveStatusResponseApi:
        checklivestatus_result = self._authentication_service_processor.checklivestatus()
        return self._mapper(checklivestatus_result, AuthenticationCheckLiveStatusResponseApi)

    def email_sign_up(self, email_sign_up_request_api: EmailSignUpRequestApi) -> EmailSignUpResponseApi:
        email_sign_up_request = self._mapper(email_sign_up_request_api, EmailSignUpRequest)
        email_sign_up_result = self._authentication_service_processor.email_sign_up(email_sign_up_request)
        return self._mapper(email_sign_up_result, EmailSignUpResponseApi)

    def email_login(self, email_sign_up_request_api: EmailSignUpRequestApi) -> EmailSignUpResponseApi:
        email_sign_up_request = self._mapper(email_sign_up_request_api, EmailSignUpRequest)
        email_sign_up_result = self._authentication_service_processor.email_login(email_sign_up_request)
        return self._mapper(email_sign_up_result, EmailSignUpResponseApi)
