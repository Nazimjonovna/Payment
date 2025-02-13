import base64
import binascii

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from Payme.serializer import MerchatTransactionsModelSerializer

from Payme.utils.logger import logged

from Payme.errors.exceptions import MethodNotFound
from Payme.errors.exceptions import PermissionDenied
from Payme.errors.exceptions import PerformTransactionDoesNotExist

from Payme.methods.check_transaction import CheckTransaction
from Payme.methods.cancel_transaction import CancelTransaction
from Payme.methods.create_transaction import CreateTransaction
from Payme.methods.perform_transaction import PerformTransaction
from Payme.methods.check_perform_transaction import CheckPerformTransaction

from drf_yasg.utils import swagger_auto_schema


class MerchantAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    @swagger_auto_schema(request_body=MerchatTransactionsModelSerializer)
    def post(self, request, *args, **kwargs):
        password = request.META.get('HTTP_AUTHORIZATION')
        if self.authorize(password):
            incoming_data: dict = request.data
            incoming_method: str = incoming_data.get("method")
            logged_message: str = "Incoming {data}"

            logged(
                logged_message=logged_message.format(
                    method=incoming_method,
                    data=incoming_data
                ),
                logged_type="info"
            )
            try:
                paycom_method = self.get_paycom_method_by_name(
                    incoming_method=incoming_method
                )
            except ValidationError:
                raise MethodNotFound()
            except PerformTransactionDoesNotExist:
                raise PerformTransactionDoesNotExist()

            paycom_method = paycom_method(incoming_data.get("params"))

        return Response(data=paycom_method)

    @staticmethod
    def get_paycom_method_by_name(incoming_method: str) -> object:
        print("method: ", incoming_method)
        available_methods: dict = {
            "CheckTransaction": CheckTransaction,
            "CreateTransaction": CreateTransaction,
            "CancelTransaction": CancelTransaction,
            "PerformTransaction": PerformTransaction,
            "CheckPerformTransaction": CheckPerformTransaction
        }

        try:
            MerchantMethod = available_methods[incoming_method]
        except Exception:
            error_message = "Unavailable method: %s" % incoming_method
            logged(
                logged_message=error_message,
                logged_type="error"
            )
            raise MethodNotFound(error_message=error_message)

        merchant_method = MerchantMethod()
        return merchant_method

    @staticmethod
    def authorize(password: str) -> None:
        """
        Authorize the Merchant.
        :param password: string -> Merchant authorization password
        """
        is_payme: bool = False
        error_message: str = ""

        if not isinstance(password, str):
            error_message = "Request from an unauthorized source!"
            logged(
                logged_message=error_message,
                logged_type="error"
            )
            raise PermissionDenied(error_message=error_message)

        password = password.split()[-1]

        try:
            password = base64.b64decode(password).decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            error_message = "Error when authorize request to merchant!"
            logged(
                logged_message=error_message,
                logged_type="error"
            )
            raise PermissionDenied(error_message=error_message)

        merchant_key = password.split(':')[-1]
        if merchant_key == settings.PAYME.get('PAYME_KEY'):
            is_payme = True

        if merchant_key != settings.PAYME.get('PAYME_KEY'):
            logged(
                logged_message="Invalid key in request!",
                logged_type="error"
            )

        if is_payme is False:
            raise PermissionDenied(
                error_message="Unavailable data for unauthorized users!"
            )

        return is_payme
