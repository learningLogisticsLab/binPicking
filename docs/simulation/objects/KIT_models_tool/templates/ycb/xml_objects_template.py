class $ObjectName(MujocoXMLObject):
    """
    $ObjectName
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("$LocationXML"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class $VisualObjectName(MujocoXMLObject):
    """
    $ObjectNamev
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("$LocationVisualXML"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

