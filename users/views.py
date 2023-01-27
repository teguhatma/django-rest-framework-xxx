from rest_framework.views import APIView
from rest_framework.response import Response


class Jobs(APIView):
    """
    API endpoint
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