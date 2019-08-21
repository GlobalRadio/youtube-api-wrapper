from copy import deepcopy
import logging
import requests

from .exceptions import *
from .utils import *



class Channel:
    def __init__(self, **kwargs):
        self.url = kwargs.get("url", None)
        self.id = kwargs.get("id", None)

        self._printable_items = [
            "url"
        ]

    def __str__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'*  {name}={param}' for name, param in items_ if name in self._printable_items])

    def __repr__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'*  {name}={param}' for name, param in items_ if name in self._printable_items])


class User:
    def __init__(self, kwargs):
        self.name = kwargs.get("authorDisplayName", "Unknown Name")
        self.avatar = kwargs.get("authorDisplayName", None)
        self.channel = Channel(
            url=kwargs.get("authorChannelUrl"),
            id=kwargs.get("authorChannelId", {}).get("value")
        )

        self._printable_items = [
            "name"
        ]

    def __str__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'*  {name}={param}' for name, param in items_ if name in self._printable_items])

    def __repr__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'*  {name}={param}' for name, param in items_ if name in self._printable_items])


class Comment:
    def __init__(self, kwargs):
        if not kwargs.get("kind") == "youtube#comment":
            raise BadKindOfResponse(f"{kwargs.get('kind')} is not right kind of Comment")
        self.id = kwargs.get("id", "")
        self._snippet = kwargs.get("snippet", {})
        self.channel = Channel(id=self._snippet.get("channelId", {}))
        self.videoId = self._snippet.get("videoId", "")
        self.display_text = self._snippet.get("textDisplay", "")
        self.text = self._snippet.get("textOriginal", "")
        self.parent = self._snippet.get("parentId", "")
        self.canRate = self._snippet.get("canRate", False)
        _liked = self._snippet.get("viewerRating", 'none')
        self.is_liked = True if _liked == 'like' else False
        self.likes = self._snippet.get("likeCount", 0)
        self.moderationStatus = self._snippet.get("moderationStatus", "")
        self.publishedAt = get_utc_from_string(self._snippet.get("publishedAt", None))
        self.updatedAt = get_utc_from_string(self._snippet.get("updatedAt", None))
        self.author = User(self._snippet)

        self._printable_items = [
            "text",
            "publishedAt"
        ]

    def __str__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'*      {name}={param}' for name, param in items_ if name in self._printable_items])

    def __repr__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'*      {name}={param}' for name, param in items_ if name in self._printable_items])


class CommentThread:
    def __init__(self, kwargs):
        if not kwargs.get("kind") == "youtube#commentThread":
            raise BadKindOfResponse(f"{kwargs.get('kind')} is not right kind of Comment Thread")
        self.id = kwargs.get("id", "")
        self._snippet = kwargs.get("snippet", {})
        self.channel = Channel(id=self._snippet.get("channelId"))
        self.videoId = self._snippet.get("videoId", "")
        self.canReply = self._snippet.get("canReply", False)
        self.isPublic = self._snippet.get("isPublic", False)
        self.replies_count = self._snippet.get("totalReplyCount", 0)
        self.topLevelComment = Comment(self._snippet.get("topLevelComment", None))
        self.replies = []
        self._replies = kwargs.get("replies", {}).get("comments", [])
        for comment in self._replies:
            self.replies.append(Comment(comment))

        self._printable_items = [
            "replies_count",
            "topLevelComment",
            "replies"
        ]

    def __str__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'+    {name}={param}' for name, param in items_ if name in self._printable_items])

    def __repr__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'+    {name}={param}' for name, param in items_ if name in self._printable_items])


class CommentThreadList:
    def __init__(self, kwargs):
        if not kwargs.get("kind") == "youtube#commentThreadListResponse":
            raise BadKindOfResponse(f"{kwargs.get('kind')} is not right kind of Comment Thread List")
        self.nextPageToken = kwargs.get("nextPageToken", None)
        self.totalResults = kwargs.get("totalResults", 0)
        self.resultsPerPage = kwargs.get("resultsPerPage", 0)
        self.comments = []
        self._items = kwargs.get("items", [])
        for comment in self._items:
            self.comments.append(CommentThread(comment))

        self._printable_items = [
            "comments"
        ]

    def __str__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'-  {name}={param}' for name, param in items_ if name in self._printable_items])

    def __repr__(self):
        items_ = self.__dict__.items()
        return f"{self.__class__.__name__}:"+"\n"+'\n'.join([f'-  {name}={param}' for name, param in items_ if name in self._printable_items])
