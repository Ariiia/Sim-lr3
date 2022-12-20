from element import Element


class Create(Element):
    def __init__(self, delay: float, delay_dev = 0.0, name = "CREATOR"):

        super().__init__(delay)
        self.name = name

    def onFinish(self):
        super().onFinish()
        self.tnext[0] = self.tcurr + self.get_delay()

        super().get_next_element().onStart()