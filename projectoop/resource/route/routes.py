from projectoop.resource.humans import Humans, HumansList


def human_routes_initialize(api):
    api.add_resource(Humans, '/humans/<int:id>', endpoint="humans")
    api.add_resource(HumansList, "/humans/", endpoint="humans_list")
