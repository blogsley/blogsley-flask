import graphene

from rx import Observable

import blogsley_flask.user.schema as users
import blogsley_flask.post.schema as blog
import blogsley_flask.image.schema as images

class Mutation(users.Mutation, blog.Mutation, images.Mutation):
    pass

class Query(users.Query, blog.Query, images.Query):
    pass

class Subscription(blog.Subscription):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
