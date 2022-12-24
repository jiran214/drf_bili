from rest_framework.response import Response
from rest_framework.views import APIView

from apps.note.models import Info
from apps.note.ser import NoteInfoSer


class TestView(APIView):
    def get(self, request):
        book_list = Info.objects.all()[:3]
        book_ser = NoteInfoSer(book_list, many=True)

        return Response(book_ser.data)

    def post(self, request):
        book_ser = NoteInfoSer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})

    def put(self, request, pk):
        book = Info.objects.all().filter(pk=pk).first()
        book_ser = NoteInfoSer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})

    def delete(self, request, pk):
        ret = Info.objects.filter(pk=pk).delete()
        return Response({'status': 100, 'msg': '删除成功'})