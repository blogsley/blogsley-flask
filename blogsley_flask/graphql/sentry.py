'''
class GraphQLResolveInfo(NamedTuple):
    field_name: str
    field_nodes: List[FieldNode]
    return_type: "GraphQLOutputType"
    parent_type: "GraphQLObjectType"
    path: Path
    schema: "GraphQLSchema"
    fragments: Dict[str, FragmentDefinitionNode]
    root_value: Any
    operation: OperationDefinitionNode
    variable_values: Dict[str, Any]
    context: Any
    is_awaitable: Callable[[Any], bool]
'''

class Sentry:
    def resolve(self, next, root, info, **kwargs):
        #print('next: ', next)
        #print('root: ', root)
        #print('info: ', info)
        #print('context: ', vars(info.context))
        print('field_name: ', info.field_name)
        return next(root, info, **kwargs)
