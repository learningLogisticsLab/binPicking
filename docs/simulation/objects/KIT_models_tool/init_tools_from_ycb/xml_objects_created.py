import numpy as np
from robosuite.models.objects import MujocoXMLObject
from robosuite.utils.mjcf_utils import xml_path_completion, array_to_string, find_elements


class BottleObject(MujocoXMLObject):
    """
    Bottle object
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/bottle.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)

class CanObject(MujocoXMLObject):
    """
    Coke can object (used in PickPlace)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/can.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)

class MasterChefCanObject(MujocoXMLObject):
    """
    MasterChef Coffee can object
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/master_chef_can.xml"),
                         name=name,
                         joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)

class LemonObject(MujocoXMLObject):
    """
    Lemon object
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/lemon.xml"),
                         name=name, obj_type="all", duplicate_collision_geoms=True)


class MilkObject(MujocoXMLObject):
    """
    Milk carton object (used in PickPlace)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/milk.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)


class BreadObject(MujocoXMLObject):
    """
    Bread loaf object (used in PickPlace)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/bread.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)


class CerealObject(MujocoXMLObject):
    """
    Cereal box object (used in PickPlace)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/cereal.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)


class SquareNutObject(MujocoXMLObject):
    """
    Square nut object (used in NutAssembly)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/square-nut.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)

    @property
    def important_sites(self):
        """
        Returns:
            dict: In addition to any default sites for this object, also provides the following entries

                :`'handle'`: Name of nut handle location site
        """
        # Get dict from super call and add to it
        dic = super().important_sites
        dic.update({
            "handle": self.naming_prefix + "handle_site"
        })
        return dic


class RoundNutObject(MujocoXMLObject):
    """
    Round nut (used in NutAssembly)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/round-nut.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)

    @property
    def important_sites(self):
        """
        Returns:
            dict: In addition to any default sites for this object, also provides the following entries

                :`'handle'`: Name of nut handle location site
        """
        # Get dict from super call and add to it
        dic = super().important_sites
        dic.update({
            "handle": self.naming_prefix + "handle_site"
        })
        return dic


class MilkVisualObject(MujocoXMLObject):
    """
    Visual fiducial of milk carton (used in PickPlace).

    Fiducial objects are not involved in collision physics.
    They provide a point of reference to indicate a position.
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/milk-visual.xml"),
                         name=name, joints=None, obj_type="visual", duplicate_collision_geoms=True)


class BreadVisualObject(MujocoXMLObject):
    """
    Visual fiducial of bread loaf (used in PickPlace)

    Fiducial objects are not involved in collision physics.
    They provide a point of reference to indicate a position.
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/bread-visual.xml"),
                         name=name, joints=None, obj_type="visual", duplicate_collision_geoms=True)


class CerealVisualObject(MujocoXMLObject):
    """
    Visual fiducial of cereal box (used in PickPlace)

    Fiducial objects are not involved in collision physics.
    They provide a point of reference to indicate a position.
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/cereal-visual.xml"),
                         name=name, joints=None, obj_type="visual", duplicate_collision_geoms=True)


class CanVisualObject(MujocoXMLObject):
    """
    Visual fiducial of coke can (used in PickPlace)

    Fiducial objects are not involved in collision physics.
    They provide a point of reference to indicate a position.
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/can-visual.xml"),
                         name=name, joints=None, obj_type="visual", duplicate_collision_geoms=True)


class MasterChefCanVisualObject(MujocoXMLObject):
    """
    Visual fiducial of masterchef can

    Fiducial objects are not involved in collision physics.
    They provide a point of reference to indicate a position.
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/master_chef_can_visual.xml"),
                         name=name,
                         joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class PlateWithHoleObject(MujocoXMLObject):
    """
    Square plate with a hole in the center (used in PegInHole)
    """

    def __init__(self, name):
        super().__init__(xml_path_completion("objects/plate-with-hole.xml"),
                         name=name, joints=None, obj_type="all", duplicate_collision_geoms=True)


class DoorObject(MujocoXMLObject):
    """
    Door with handle (used in Door)

    Args:
        friction (3-tuple of float): friction parameters to override the ones specified in the XML
        damping (float): damping parameter to override the ones specified in the XML
        lock (bool): Whether to use the locked door variation object or not
    """
    def __init__(self, name, friction=None, damping=None, lock=False):
        xml_path = "objects/door.xml"
        if lock:
            xml_path = "objects/door_lock.xml"
        super().__init__(xml_path_completion(xml_path),
                         name=name, joints=None, obj_type="all", duplicate_collision_geoms=True)

        # Set relevant body names
        self.door_body = self.naming_prefix + "door"
        self.frame_body = self.naming_prefix + "frame"
        self.latch_body = self.naming_prefix + "latch"
        self.hinge_joint = self.naming_prefix + "hinge"

        self.lock = lock
        self.friction = friction
        self.damping = damping
        if self.friction is not None:
            self._set_door_friction(self.friction)
        if self.damping is not None:
            self._set_door_damping(self.damping)

    def _set_door_friction(self, friction):
        """
        Helper function to override the door friction directly in the XML

        Args:
            friction (3-tuple of float): friction parameters to override the ones specified in the XML
        """
        hinge = find_elements(root=self.worldbody, tags="joint", attribs={"name": self.hinge_joint}, return_first=True)
        hinge.set("frictionloss", array_to_string(np.array([friction])))

    def _set_door_damping(self, damping):
        """
        Helper function to override the door friction directly in the XML

        Args:
            damping (float): damping parameter to override the ones specified in the XML
        """
        hinge = find_elements(root=self.worldbody, tags="joint", attribs={"name": self.hinge_joint}, return_first=True)
        hinge.set("damping", array_to_string(np.array([damping])))

    @property
    def important_sites(self):
        """
        Returns:
            dict: In addition to any default sites for this object, also provides the following entries

                :`'handle'`: Name of door handle location site
        """
        # Get dict from super call and add to it
        dic = super().important_sites
        dic.update({
            "handle": self.naming_prefix + "handle"
        })
        return dic

# BinPicking objects and visuals (choosing to append just a 'v' for ease)
# Defs: https://github.com/learningLogisticsLab/binPicking/blob/main/docs/simulation/objects/object_categories_db.xlsx



class bottl(MujocoXMLObject):
    """
    bottl
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/bottle.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class bottlv(MujocoXMLObject):
    """
    bottlv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/bottlv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class bread(MujocoXMLObject):
    """
    bread
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/bread-visual.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class breadv(MujocoXMLObject):
    """
    breadv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/breadv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class bread(MujocoXMLObject):
    """
    bread
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/bread.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class breadv(MujocoXMLObject):
    """
    breadv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/breadv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class can-v(MujocoXMLObject):
    """
    can-v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/can-visual.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class can-vv(MujocoXMLObject):
    """
    can-vv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/can-vv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class can.x(MujocoXMLObject):
    """
    can.x
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/can.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class can.xv(MujocoXMLObject):
    """
    can.xv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/can.xv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class cerea(MujocoXMLObject):
    """
    cerea
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/cereal-visual.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class cereav(MujocoXMLObject):
    """
    cereav
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/cereav.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class cerea(MujocoXMLObject):
    """
    cerea
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/cereal.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class cereav(MujocoXMLObject):
    """
    cereav
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/cereav.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class door.(MujocoXMLObject):
    """
    door.
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/door.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class door.v(MujocoXMLObject):
    """
    door.v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/door.v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class door_(MujocoXMLObject):
    """
    door_
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/door_lock.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class door_v(MujocoXMLObject):
    """
    door_v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/door_v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class lemon(MujocoXMLObject):
    """
    lemon
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/lemon.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class lemonv(MujocoXMLObject):
    """
    lemonv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/lemonv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class maste(MujocoXMLObject):
    """
    maste
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/master_chef_can-visual.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class mastev(MujocoXMLObject):
    """
    mastev
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/mastev.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class maste(MujocoXMLObject):
    """
    maste
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/master_chef_can.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class mastev(MujocoXMLObject):
    """
    mastev
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/mastev.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class milk.(MujocoXMLObject):
    """
    milk.
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/milk.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class milk.v(MujocoXMLObject):
    """
    milk.v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/milk.v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0001(MujocoXMLObject):
    """
    o0001
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0001.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0001v(MujocoXMLObject):
    """
    o0001v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0001v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0002(MujocoXMLObject):
    """
    o0002
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0002.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0002v(MujocoXMLObject):
    """
    o0002v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0002v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0003(MujocoXMLObject):
    """
    o0003
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0003.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0003v(MujocoXMLObject):
    """
    o0003v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0003v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0004(MujocoXMLObject):
    """
    o0004
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0004.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0004v(MujocoXMLObject):
    """
    o0004v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0004v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0005(MujocoXMLObject):
    """
    o0005
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0005.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0005v(MujocoXMLObject):
    """
    o0005v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0005v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0006(MujocoXMLObject):
    """
    o0006
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0006.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0006v(MujocoXMLObject):
    """
    o0006v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0006v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0007(MujocoXMLObject):
    """
    o0007
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0007.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0007v(MujocoXMLObject):
    """
    o0007v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0007v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0008(MujocoXMLObject):
    """
    o0008
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0008.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0008v(MujocoXMLObject):
    """
    o0008v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0008v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0009(MujocoXMLObject):
    """
    o0009
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0009.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0009v(MujocoXMLObject):
    """
    o0009v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0009v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0010(MujocoXMLObject):
    """
    o0010
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0010.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0010v(MujocoXMLObject):
    """
    o0010v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0010v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0011(MujocoXMLObject):
    """
    o0011
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0011.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0011v(MujocoXMLObject):
    """
    o0011v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0011v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0012(MujocoXMLObject):
    """
    o0012
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0012.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0012v(MujocoXMLObject):
    """
    o0012v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0012v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0013(MujocoXMLObject):
    """
    o0013
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0013.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0013v(MujocoXMLObject):
    """
    o0013v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0013v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0014(MujocoXMLObject):
    """
    o0014
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0014.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0014v(MujocoXMLObject):
    """
    o0014v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0014v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0015(MujocoXMLObject):
    """
    o0015
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0015.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0015v(MujocoXMLObject):
    """
    o0015v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0015v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0016(MujocoXMLObject):
    """
    o0016
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0016.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0016v(MujocoXMLObject):
    """
    o0016v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0016v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0017(MujocoXMLObject):
    """
    o0017
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0017.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0017v(MujocoXMLObject):
    """
    o0017v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0017v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0018(MujocoXMLObject):
    """
    o0018
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0018.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0018v(MujocoXMLObject):
    """
    o0018v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0018v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0019(MujocoXMLObject):
    """
    o0019
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0019.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0019v(MujocoXMLObject):
    """
    o0019v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0019v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0020(MujocoXMLObject):
    """
    o0020
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0020.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0020v(MujocoXMLObject):
    """
    o0020v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0020v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0021(MujocoXMLObject):
    """
    o0021
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0021.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0021v(MujocoXMLObject):
    """
    o0021v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0021v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0022(MujocoXMLObject):
    """
    o0022
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0022.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0022v(MujocoXMLObject):
    """
    o0022v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0022v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0023(MujocoXMLObject):
    """
    o0023
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0023.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0023v(MujocoXMLObject):
    """
    o0023v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0023v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0024(MujocoXMLObject):
    """
    o0024
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0024.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0024v(MujocoXMLObject):
    """
    o0024v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0024v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0025(MujocoXMLObject):
    """
    o0025
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0025.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0025v(MujocoXMLObject):
    """
    o0025v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0025v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0026(MujocoXMLObject):
    """
    o0026
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0026.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0026v(MujocoXMLObject):
    """
    o0026v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0026v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0027(MujocoXMLObject):
    """
    o0027
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0027.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0027v(MujocoXMLObject):
    """
    o0027v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0027v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0028(MujocoXMLObject):
    """
    o0028
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0028.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0028v(MujocoXMLObject):
    """
    o0028v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0028v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0029(MujocoXMLObject):
    """
    o0029
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0029.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0029v(MujocoXMLObject):
    """
    o0029v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0029v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0030(MujocoXMLObject):
    """
    o0030
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0030.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0030v(MujocoXMLObject):
    """
    o0030v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0030v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0031(MujocoXMLObject):
    """
    o0031
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0031.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0031v(MujocoXMLObject):
    """
    o0031v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0031v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0032(MujocoXMLObject):
    """
    o0032
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0032.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0032v(MujocoXMLObject):
    """
    o0032v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0032v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0033(MujocoXMLObject):
    """
    o0033
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0033.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0033v(MujocoXMLObject):
    """
    o0033v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0033v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0034(MujocoXMLObject):
    """
    o0034
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0034.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0034v(MujocoXMLObject):
    """
    o0034v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0034v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0035(MujocoXMLObject):
    """
    o0035
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0035.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0035v(MujocoXMLObject):
    """
    o0035v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0035v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0036(MujocoXMLObject):
    """
    o0036
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0036.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0036v(MujocoXMLObject):
    """
    o0036v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0036v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0037(MujocoXMLObject):
    """
    o0037
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0037.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0037v(MujocoXMLObject):
    """
    o0037v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0037v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0038(MujocoXMLObject):
    """
    o0038
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0038.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0038v(MujocoXMLObject):
    """
    o0038v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0038v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0039(MujocoXMLObject):
    """
    o0039
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0039.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0039v(MujocoXMLObject):
    """
    o0039v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0039v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0040(MujocoXMLObject):
    """
    o0040
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0040.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0040v(MujocoXMLObject):
    """
    o0040v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0040v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0041(MujocoXMLObject):
    """
    o0041
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0041.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0041v(MujocoXMLObject):
    """
    o0041v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0041v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0042(MujocoXMLObject):
    """
    o0042
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0042.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0042v(MujocoXMLObject):
    """
    o0042v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0042v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0043(MujocoXMLObject):
    """
    o0043
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0043.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0043v(MujocoXMLObject):
    """
    o0043v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0043v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0044(MujocoXMLObject):
    """
    o0044
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0044.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0044v(MujocoXMLObject):
    """
    o0044v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0044v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0045(MujocoXMLObject):
    """
    o0045
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0045.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0045v(MujocoXMLObject):
    """
    o0045v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0045v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0046(MujocoXMLObject):
    """
    o0046
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0046.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0046v(MujocoXMLObject):
    """
    o0046v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0046v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0047(MujocoXMLObject):
    """
    o0047
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0047.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0047v(MujocoXMLObject):
    """
    o0047v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0047v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0048(MujocoXMLObject):
    """
    o0048
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0048.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0048v(MujocoXMLObject):
    """
    o0048v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0048v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0049(MujocoXMLObject):
    """
    o0049
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0049.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0049v(MujocoXMLObject):
    """
    o0049v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0049v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0050(MujocoXMLObject):
    """
    o0050
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0050.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0050v(MujocoXMLObject):
    """
    o0050v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0050v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0051(MujocoXMLObject):
    """
    o0051
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0051.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0051v(MujocoXMLObject):
    """
    o0051v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0051v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0052(MujocoXMLObject):
    """
    o0052
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0052.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0052v(MujocoXMLObject):
    """
    o0052v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0052v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0053(MujocoXMLObject):
    """
    o0053
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0053.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0053v(MujocoXMLObject):
    """
    o0053v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0053v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0054(MujocoXMLObject):
    """
    o0054
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0054.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0054v(MujocoXMLObject):
    """
    o0054v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0054v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0055(MujocoXMLObject):
    """
    o0055
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0055.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0055v(MujocoXMLObject):
    """
    o0055v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0055v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0056(MujocoXMLObject):
    """
    o0056
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0056.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0056v(MujocoXMLObject):
    """
    o0056v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0056v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0057(MujocoXMLObject):
    """
    o0057
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0057.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0057v(MujocoXMLObject):
    """
    o0057v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0057v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0058(MujocoXMLObject):
    """
    o0058
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0058.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0058v(MujocoXMLObject):
    """
    o0058v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0058v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0059(MujocoXMLObject):
    """
    o0059
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0059.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0059v(MujocoXMLObject):
    """
    o0059v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0059v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0060(MujocoXMLObject):
    """
    o0060
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0060.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0060v(MujocoXMLObject):
    """
    o0060v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0060v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0061(MujocoXMLObject):
    """
    o0061
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0061.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0061v(MujocoXMLObject):
    """
    o0061v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0061v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0062(MujocoXMLObject):
    """
    o0062
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0062.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0062v(MujocoXMLObject):
    """
    o0062v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0062v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0063(MujocoXMLObject):
    """
    o0063
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0063.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0063v(MujocoXMLObject):
    """
    o0063v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0063v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0064(MujocoXMLObject):
    """
    o0064
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0064.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0064v(MujocoXMLObject):
    """
    o0064v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0064v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0065(MujocoXMLObject):
    """
    o0065
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0065.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0065v(MujocoXMLObject):
    """
    o0065v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0065v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0066(MujocoXMLObject):
    """
    o0066
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0066.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0066v(MujocoXMLObject):
    """
    o0066v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0066v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0067(MujocoXMLObject):
    """
    o0067
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0067.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0067v(MujocoXMLObject):
    """
    o0067v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0067v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0068(MujocoXMLObject):
    """
    o0068
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0068.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0068v(MujocoXMLObject):
    """
    o0068v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0068v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class o0069(MujocoXMLObject):
    """
    o0069
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0069.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class o0069v(MujocoXMLObject):
    """
    o0069v
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/o0069v.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class plate(MujocoXMLObject):
    """
    plate
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/plate-with-hole.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class platev(MujocoXMLObject):
    """
    platev
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/platev.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class round(MujocoXMLObject):
    """
    round
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/round-nut.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class roundv(MujocoXMLObject):
    """
    roundv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/roundv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

class squar(MujocoXMLObject):
    """
    squar
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/square-nut.xml"),
                         name=name, joints=[dict(type="free", damping="0.0005")],
                         obj_type="all", duplicate_collision_geoms=True)
                         

class squarv(MujocoXMLObject):
    """
    squarv
    """
    def __init__(self, name):
        super().__init__(xml_path_completion("./objects/squarv.xml"),
                         name=name, joints=None,
                         obj_type="visual", duplicate_collision_geoms=True)

