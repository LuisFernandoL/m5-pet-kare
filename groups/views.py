from rest_framework.views import Request, Response, APIView, status
from .serializers import GroupSerializer
from .models import Group

class GroupView(APIView):
    def post(self, req: Request) -> Response:
        serializer = GroupSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        group = Group.objects.create(**serializer.validated_data)
        serializer = GroupSerializer(group)
        return Response(serializer.data, status.HTTP_201_CREATED)