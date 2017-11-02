
import inspect
import traceback


class cls(object):
    
    def attr_gen(self):
        attrs = set(dir(self)) - set(dir(object))
        for attr in attrs:
            a = getattr(self, attr, None)
            if a is not None and type(a) is not np.ndarray and not(inspect.isfunction(a) or inspect.ismethod(a) or inspect.isclass(a)):
                yield attr.upper()
                yield a
    def printState(self):
        nprint('Tree Attributes:', *self.attr_gen())
        nprint('\n\n')
        
    def nprint(farg, *args):
        print ''.join(traceback.format_stack())
        print farg
        for arg in args:
          print arg


