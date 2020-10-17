from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Member
)
from .serializers import(
    MemberSerializer
)

"""
By default the field role is false which is not admin.
To Change it to admin pass true in the Post data.
"""

@api_view(['POST'])
def add_member(request):
    serilaizer = MemberSerializer(data=request.data)
    if serilaizer.is_valid():
        member = serilaizer.save()
        if member:
            return Response(serilaizer.data,status=status.HTTP_201_CREATED)
    return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_member(request):
    all_members = Member.objects.all()
    serilaizer = MemberSerializer(all_members,many=True)
    if serilaizer:
        return Response(serilaizer.data,status=status.HTTP_200_OK)
    return Response({"response":"no_members"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def edit_member(request):

    member_id = Member.objects.filter(id=request.data.get("id"))

    if not member_id.exists():
        return Response({"response":"member_not_found"},status=status.HTTP_400_BAD_REQUEST)

    member_id = member_id.first()

    serilaizer = MemberSerializer(member_id,data=request.data,partial=True)
    if serilaizer.is_valid():
        member = serilaizer.save()
        if member:
            return Response(serilaizer.data,status=status.HTTP_200_OK)
    return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

  

@api_view(['DELETE'])
def delete_member(request):
    if "id" not in request.data:
        return Response({"response":"id_required"},status=status.HTTP_400_BAD_REQUEST)

    member = Member.objects.filter(id=request.data.get("id"))

    if not member.exists():
        return Response({"response":"member_not_found"},status=status.HTTP_400_BAD_REQUEST)

    if member.exists():
        member.delete()
        return Response({"response":"deleted_successfully"},status=status.HTTP_200_OK)
    return Response({"response":"not_found"},status=status.HTTP_400_BAD_REQUEST)