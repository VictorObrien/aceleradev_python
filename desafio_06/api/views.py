from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter
from rest_framework.response import Response


@api_view(["POST"])
def lambda_function(request):
    try:
        question = request.data.get("question")
        response_list = []
        for numero_lista in Counter(question).most_common():
            for contador in range(0, numero_lista[1]):
                response_list.append(numero_lista[0])
        return Response({"solution": response_list})

    except KeyError:
        return Response(
            {'detail': 'Invalid request, a JSON containing the question key and a list '
                       'is expected. e.g. {"question": [2, 5, 4, 3, 3, 5, 3, 2]}'},
            status=status.HTTP_400_BAD_REQUEST
        )
