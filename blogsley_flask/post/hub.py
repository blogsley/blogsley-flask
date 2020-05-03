from loguru import logger

import graphene

from blogsley_flask.hub import Hub, Subscriber

hub = Hub()

class PostEvent(graphene.ObjectType):
    kind = graphene.String()
    def __init__(self, id, kind='UPDATE'):
        super().__init__()
        self.id = id
        self.kind = kind

    def __repr__(self):
        return f"<PostEvent id={self.id} kind={self.kind}>"

class PostSubscriber(Subscriber):
    def __init__(self, observer, id):
        super().__init__(observer)
        self.id = id

    def send(self, msg):
        logger.debug(f"sending")
        logger.debug(f"myid: {self.id}")
        logger.debug(f"msg: {msg}")
        if msg.id != self.id:
            return
        super().send(msg)
