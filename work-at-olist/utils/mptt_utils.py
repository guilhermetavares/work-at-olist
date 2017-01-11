
def recursive_mptt_to_dict(instance, serializer, method='get_children', key='childrens'):
    result = serializer(instance).data
    childrens = [recursive_mptt_to_dict(children, serializer, method) for children in getattr(instance, method)()]
    if childrens:
        result[key] = childrens
    return result