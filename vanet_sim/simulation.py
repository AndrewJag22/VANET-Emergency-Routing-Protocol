"""Contains code to run the simulations."""

__author__ = 'Adam Morrissett', 'Steven M. Hernandez'

from vanet_sim.evaluation import Evaluations
from vanet_sim.routing.urban_routing_protocol import UrbanRoutingProtocol


class Simulation:
    """Performs a simulation."""

    def __init__(self, d_time, road_map, vehicle_net):
        """Custom constructor that initializes parameters.

        :param d_time: simulation time resolution
        :param road_map: filepath of the road network config file
        :param vehicle_net: filepath of the vehicle network config file
        """
        self.cur_time = 0
        self.d_time = d_time
        self.road_net = road_map
        self.vehicle_net = vehicle_net

    def step(self):
<<<<<<< HEAD
        """Progresses the simulation forward by one time derivative."""

=======
        # Update vehicle locations first
>>>>>>> f2eb4b098e4fe245f7859a011ee7ab6da3a5c0de
        for vehicle in self.vehicle_net:
            vehicle.update_location(self.cur_time)

        # Collect list of neighbors
        for vehicle in self.vehicle_net:
            vehicle.update_neighbors(self.vehicle_net)

        # Find the current forwarders
        current_forwarders = []
        for vehicle in self.vehicle_net:
            if vehicle.is_current_forwarder:
                current_forwarders.append(vehicle)

        # Route the message from the current forwarder
        for f_curr in current_forwarders:
            protocol = UrbanRoutingProtocol
            f_next = protocol.choose_next_forwarder(f_curr.neighbors)
            if f_next is not None:
                self.vehicle_net[f_curr.id - 1].is_current_forwarder = False
                self.vehicle_net[f_next.id - 1].received_at = self.cur_time
                self.vehicle_net[f_next.id - 1].is_current_forwarder = True

        print(Evaluations.run(self.cur_time, self.vehicle_net))

        self.cur_time += self.d_time

    def run(self, time_duration):
        """Executes the simulation for the specified duration.

        This is on top of previous simulation time.
        """

        print(f'Starting simulation from t = {self.cur_time:.3f}')

        while self.cur_time < time_duration:
            self.step()
