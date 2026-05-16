class Parent(object):
    # parent's method to be overriden
    def override(self):
        print("PARENT override()")
    # parent's method to be implicited
    def implicit(self):
        print("PARENT implicit()")
    # parent's method to be altered
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    # implicit() is not defined here — Child inherits it from Parent as-is
    def override(self):
        print("CHILD override()")
    # Child inherits Parent's method and alters it
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # we call the original Parent's method
        super(Child, self).altered()
        # we alter the original Parent's method 
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()