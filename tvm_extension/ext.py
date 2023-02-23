from tvm.driver.tvmc.extensions import TVMExtension
from .backend import VanillaAcceleratorBackend

class MyExt(TVMExtension):
  def __init__(self):
    self.backend = VanillaAcceleratorBackend()

  def uma_backends(self):
    return [self.backend]
