"""
This type stub file was generated by pyright.
"""

from .mountedtype import MountedType

base_type = type

def source_resolver(source, root, info, **args): ...

class Field(MountedType):
    """
    Makes a field available on an ObjectType in the GraphQL schema. Any type can be mounted as a
    Field:

    - Object Type
    - Scalar Type
    - Enum
    - Interface
    - Union

    All class attributes of ``graphene.ObjectType`` are implicitly mounted as Field using the below
    arguments.

    .. code:: python

        class Person(ObjectType):
            first_name = graphene.String(required=True)                # implicitly mounted as Field
            last_name = graphene.Field(String, description='Surname')  # explicitly mounted as Field

    args:
        type (class for a graphene.UnmountedType): must be a class (not an instance) of an
            unmounted graphene type (ex. scalar or object) which is used for the type of this
            field in the GraphQL schema.
        args (optional, Dict[str, graphene.Argument]): arguments that can be input to the field.
            Prefer to use **extra_args.
        resolver (optional, Callable): A function to get the value for a Field from the parent
            value object. If not set, the default resolver method for the schema is used.
        source (optional, str): attribute name to resolve for this field from the parent value
            object. Alternative to resolver (cannot set both source and resolver).
        deprecation_reason (optional, str): Setting this value indicates that the field is
            depreciated and may provide instruction or reason on how for clients to proceed.
        required (optional, bool): indicates this field as not null in the graphql scehma. Same behavior as
            graphene.NonNull. Default False.
        name (optional, str): the name of the GraphQL field (must be unique in a type). Defaults to attribute
            name.
        description (optional, str): the description of the GraphQL field in the schema.
        default_value (optional, Any): Default value to resolve if none set from schema.
        **extra_args (optional, Dict[str, Union[graphene.Argument, graphene.UnmountedType]): any
            additional arguments to mount on the field.
    """

    def __init__(
        self,
        type,
        args=...,
        resolver=...,
        source=...,
        deprecation_reason=...,
        name=...,
        description=...,
        required=...,
        _creation_counter=...,
        default_value=...,
        **extra_args
    ) -> None: ...
    @property
    def type(self): ...
    def get_resolver(self, parent_resolver): ...