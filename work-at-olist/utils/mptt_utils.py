
def recursive_mptt_to_dict(instance, serializer):
    result = serializer(instance).data
    childrens = [recursive_mptt_to_dict(children, serializer) for children in instance.get_children()]
    if childrens:
        result['childrens'] = childrens
    return result