from modules.simualation import Simulation

class TestSimulation:
    def setup_method(self):
        self.simulation = Simulation()

    def test_get_rabbits(self):
        assert self.simulation.get_rabbits_num() == 100

    def test_add_rabbits_num(self):
        self.simulation.add_rabbits_num(50)
        assert self.simulation.get_rabbits_num() == 150

    def test_get_inserted(self):
        assert self.simulation.get_inserted() == 0
    
    def test_increment_inserted(self):
        self.simulation.increment_inserted()
        assert self.simulation.get_inserted() == 1