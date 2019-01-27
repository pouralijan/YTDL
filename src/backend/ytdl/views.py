from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    )

from .serializers import MyStreamSerializer
from pytube import YouTube

#class ArticleListView(ListAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer
#
#class Check(ListAPIView):
#    queryset = ["a", "b"]
#    serializer_class = ArticleSerializer
#
#class ArticleDetailView(RetrieveAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer
#
#class ArticleCreateView(CreateAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer
# url = "https://www.youtube.com/watch?v=uZgRbnIsgrA"
# ytdl = YouTube(url)
# videos_list = ytdl.streams.filter(adaptive=True).all()
class show(ListAPIView):
    queryset = []
    serializer_class = MyStreamSerializer

    def get_queryset(self):
        req = self.request
        url = req.query_params.get("url")
        ytdl = YouTube(url)
        videos_list = ytdl.streams.filter(adaptive=True).all()
        self.queryset = videos_list
        return self.queryset



# def Check(request):
#     res = {
#         'status': 'faild'
#     }
#     url = "a"
#     if request.method == "GET":
#         url = request.GET["url"]
#         ytdl = YouTube(url)
#         videos_list = ytdl.streams.filter(adaptive=True).all()
#         videos_list = []
#         for stream in ytdl.streams.all():
#             a = {
#                     "mime_type": stream.mime_type,
#                     "res": stream.resolution,
#                     "fps": stream.fps,
#                 }
#             videos_list.append(a)
#         res = {
#             'status': 'ok',
#             'url': url,
#             'videos': videos_list
#         }
#     # res = {"status": "ok", "url": url, "videos": [{"mime_type": "video/mp4", "res": "720p", "fps": 30}, {"mime_type": "video/webm", "res": "360p", "fps": 30}, {"mime_type": "video/mp4", "res": "360p", "fps": 30}, {"mime_type": "video/mp4", "res": "1080p", "fps": 30}, {"mime_type": "video/webm", "res": "1080p", "fps": 30}, {"mime_type": "video/mp4", "res": "1080p", "fps": 60}, {"mime_type": "video/webm", "res": "1080p", "fps": 60}, {"mime_type": "video/mp4", "res": "720p", "fps": 30}, {"mime_type": "video/webm", "res": "720p", "fps": 30}, {"mime_type": "video/mp4", "res": "720p", "fps": 60}, {"mime_type": "video/webm", "res": "720p", "fps": 60}, {"mime_type": "video/mp4", "res": "480p", "fps": 30}, {"mime_type": "video/webm", "res": "480p", "fps": 30}, {"mime_type": "video/mp4", "res": "360p", "fps": 30}, {"mime_type": "video/webm", "res": "360p", "fps": 30}, {"mime_type": "video/mp4", "res": "240p", "fps": 30}, {"mime_type": "video/webm", "res": "240p", "fps": 30}, {"mime_type": "video/mp4", "res": "144p", "fps": 30}, {"mime_type": "video/webm", "res": "144p", "fps": 30}, {"mime_type": "audio/mp4", "res": 'null', "fps": 30}, {"mime_type": "audio/webm", "res": 'null', "fps": 30}, {"mime_type": "audio/webm", "res": 'null', "fps": 30}, {"mime_type": "audio/webm", "res": 'null', "fps": 30}, {"mime_type": "audio/webm", "res": 'null', "fps": 30}]}

#     return JsonResponse(res)