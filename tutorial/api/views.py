from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
class ListUsers(APIView):
    def get(self, request):
        return Response({
            'msg': 'success'
        })

class NoteList(APIView):
	def get(self, request):
		stocks = Note.objects.all()
		serializer = NoteSerializer(stocks, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = NoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
	def put(self, request, pk):
		stock = get_object_or_404(Note, pk=pk)
		serializer = NoteSerializer(stock, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		stock = get_object_or_404(Note, pk=pk)
		stock.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)