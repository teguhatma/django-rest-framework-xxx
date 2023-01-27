from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Jobs(APIView):
    """
    API endpoint
    """

    def get(self, request, format=None):
        print(request.query_params.get("id"))
        if request.query_params.get("error") == "400":
            return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.query_params.get("error") == "500":
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            data = [
                {
                    "id": 1,
                    "job": "Backend Engineer",
                    "errors": {},
                    "company_name": "Google",
                    "company_url": "https://www.google.com",
                    "location": "Mountain View, CA",
                    "title": "Backend Engineer"
                },
                {
                    "id": 2,
                    "job": "Backend Developer",
                    "errors": {},
                    "company_name": "Google",
                    "company_url": "https://www.google.com",
                    "location": "Mountain View, CA",
                    "title": "Backend Engineer"
                }
            ]
            return Response({"data": data})