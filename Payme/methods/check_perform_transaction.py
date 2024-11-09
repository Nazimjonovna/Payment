from Payme.utils.get_params import get_params

from Payme.serializer import MerchatTransactionsModelSerializer


class CheckPerformTransaction:
    def __call__(self, params: dict) -> dict:
        serializer = MerchatTransactionsModelSerializer(
            data=get_params(params)
        )
        serializer.is_valid(raise_exception=True)
        print(serializer.data)

        response = {
            "result": {
                "allow": True,
                }
            }

        return response