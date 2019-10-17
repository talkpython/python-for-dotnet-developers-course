import ctypes


# We use ctypes module  to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


def refs(obj_id) -> int:
    obj = PyObject.from_address(obj_id)
    return obj.refcnt
