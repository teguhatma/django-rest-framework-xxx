from rest_framework.views import APIView
from rest_framework.response import Response


class ListApi(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get(self, request, format=None):
        data = [
            {
                "job": "Backend Engineer",
                "errors": {},
                "company_name": "Google",
                "company_url": "https://www.google.com",
                "location": "Mountain View, CA",
                "title": "Backend Engineer"
            },
            {
                "job": "Backend Developer",
                "errors": {},
                "company_name": "Google",
                "company_url": "https://www.google.com",
                "location": "Mountain View, CA",
                "title": "Backend Engineer"
            }
        ]
        return Response({"data": data})