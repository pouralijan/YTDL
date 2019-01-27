from rest_framework import serializers
from pytube import Stream

class MyStreamSerializer(serializers.Serializer):
    # self.abr = None   # average bitrate (audio streams only)
    # self.fps = None   # frames per second (video streams only)
    # self.itag = None  # stream format id (youtube nomenclature)
    # self.res = None   # resolution (e.g.: 480p, 720p, 1080p)
    # self.url = None   # signed download url

    # self._filesize = None  # filesize in bytes
    # self.mime_type = None  # content identifier (e.g.: video/mp4)
    # self.type = None       # the part of the mime before the slash
    # self.subtype = None    # the part of the mime after the slash

    # self.codecs = []         # audio/video encoders (e.g.: vp8, mp4a)
    # self.audio_codec = None  # audio codec of the stream (e.g.: vorbis)
    # self.video_codec = None  # video codec 

    abr = serializers.CharField(max_length=200)
    fps = serializers.CharField(max_length=200)
    itag = serializers.CharField(max_length=200)
    resolution = serializers.CharField(max_length=200)
    url = serializers.CharField(max_length=200)
    _filesize = serializers.CharField(max_length=200)
    mime_type = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=200)
    subtype = serializers.CharField(max_length=200)
    codecs = serializers.CharField(max_length=200)
    audio_codec = serializers.CharField(max_length=200)
    video_codec = serializers.CharField(max_length=200)

