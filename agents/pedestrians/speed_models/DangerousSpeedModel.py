from .SpeedModel import SpeedModel

class DangerousSpeedModel(SpeedModel):
    
    def initialize(self):
        self._desiredSpeed = self.internalFactors["desired_speed"] * 1.6 * 20
        self._minSpeed = self.internalFactors["min_crossing_speed"] * 1 *10
        self._maxSpeed = self.internalFactors["max_crossing_speed"] * 1.8 * 30
        self._relaxationTime = self.internalFactors["relaxation_time"] * 2 * 0.1
        pass