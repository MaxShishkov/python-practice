class Parent(object):
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        super(Child, self).show_info()
        print ("Number of torys - " + str(self.number_of_toys))

john_smith = Parent("Smith", "blue")
alan_smith = Child("Smith", "blue", 5)
alan_smith.show_info()
