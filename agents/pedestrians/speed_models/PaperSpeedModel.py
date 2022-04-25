from .SpeedModel import SpeedModel

class PaperSpeedModel(SpeedModel):
    
    def initialize(self):
        self._desiredSpeed = self.internalFactors["desired_speed"] * 1.6
        self._minSpeed = self.internalFactors["min_crossing_speed"] * 1
        self._maxSpeed = self.internalFactors["max_crossing_speed"] * 1.8
        self._relaxationTime = self.internalFactors["relaxation_time"] * 2
        pass