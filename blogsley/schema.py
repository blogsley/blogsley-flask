import graphene

from rx import Observable

import blogsley.user.schema as users
import blogsley.post.schema as blog
import blogsley.image.schema as images

class Mutation(users.Mutation, blog.Mutation, images.Mutation):
    pass

class Query(users.Query, blog.Query, images.Query):
    pass

class Subscription(blog.Subscription):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
