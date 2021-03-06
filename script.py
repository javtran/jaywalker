import carla
import random
import time
import math

from lib import SimulationVisualization, MapNames, MapManager, Simulator

SpawnActor = carla.command.SpawnActor
def get_transform(vehicle_location, angle, d=6.4):
    a = math.radians(angle)
    location = carla.Location(d * math.cos(a), d * math.sin(a), 2.0) + vehicle_location
    return carla.Transform(location, carla.Rotation(yaw=180 + angle, pitch=-15))

def main():
    
    # CONNECT CLIENT TO SERVER
    print(f"connecting to remote: 127.0.0.1:2000")
    client = carla.Client("127.0.0.1",2000)
    client.set_timeout(10.0)
    print(f"connected to remote: 127.0.0.1:2000")

    # GETTING THE MAPMANAGER AND LOADING MAP
    mapManager = MapManager(client)
    #mapManager.load(MapNames.Town02_Opt)
    client.load_world('Town02_Opt', carla.MapLayer.NONE)

    world = client.get_world()
    visualizer = SimulationVisualization(client, mapManager)

    map = world.get_map()

    # DRAW SPAWNPOINTS
    # visualizer.drawSpawnPoints()

    # CREATING OUR SPAWN POINTS FOR PEDESTRIANS
    ped_spawn_points = list()
    for i in range(3):
        spawn_point = carla.Transform()
        random_map_loc = world.get_random_location_from_navigation() # gets a valid random location on the map (not on the streets)
        if (random_map_loc != None):
            spawn_point.location = random_map_loc
            ped_spawn_points.append(spawn_point)

    #visualizer.drawWalkerNavigationPoints(spawn_points)

    # GET BLUEPRINTS FOR PEDS AND VEHICLES
    blueprintLibrary = world.get_blueprint_library()
    peds = blueprintLibrary.filter("walker.pedestrian.*")
    vehicles = blueprintLibrary.filter("vehicle.*")

    # SPAWN PEDS
    batch_ped = list()
    for spawn_point in ped_spawn_points:
        walker_bp = random.choice(peds)
        batch_ped.append(SpawnActor(walker_bp, spawn_point))
    
    ped_list = []
    for i in client.apply_batch_sync(batch_ped, True):
        if not i.error:
            print("SPAWNED A PEDESTRIAN")
            ped_list.append(i.actor_id)





    # SPAWN CARS
    car_spawn_points = mapManager.spawn_points
    batch_car = list()
    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_global_distance_to_leading_vehicle(2.5)
    SetAutopilot = carla.command.SetAutopilot
    FutureActor = carla.command.FutureActor
    for i in range(3):
        car_bp = random.choice(vehicles)
        if car_bp.has_attribute('driver_id'):
            driver_id = random.choice(car_bp.get_attribute('driver_id').recommended_values)
            car_bp.set_attribute('driver_id', driver_id)
        else:
            car_bp.set_attribute('role_name', 'autopilot')
        batch_car.append(SpawnActor(car_bp, car_spawn_points[i]).then(SetAutopilot(FutureActor, True, traffic_manager.get_port())))
    vehicles_list = []
    for i in client.apply_batch_sync(batch_car, True):
        if not i.error:
            print("SPAWNED A CAR")
            vehicles_list.append(i.actor_id)

    # CAMERA
    #camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
    # camera_bp.set_attribute('image_size_x', str(1000))
    # camera_bp.set_attribute('image_size_y', str(562))
    # camera = world.spawn_actor(camera_bp, spectator.get_transform(), attach_to = vehicles_list[0])
    


    # onTickers = [visualizer.onTick]
    # onEnders = []
    # simulator = Simulator(client, onTickers=onTickers, onEnders=onEnders)
    # simulator.run(1000)

    spectator = world.get_spectator()
    vehicle = world.get_actor(vehicles_list[0])
    pedestrian = world.get_actor(ped_list[0])

    world.set_pedestrians_cross_factor(1)
    walker_controller_bp = world.get_blueprint_library().find('controller.ai.walker')
    walkerControllerActor = world.spawn_actor(walker_controller_bp, carla.Transform(), pedestrian)
    walkerControllerActor.start()
    walkerControllerActor.go_to_location(world.get_random_location_from_navigation())
    walkerControllerActor.set_max_speed(2)
    # control = carla.WalkerControl()
    # control.speed = 1.9
    # control.direction.y = 1
    # control.direction.x = 0
    # control.direction.z = 0
    for i in range(3000):
        world.tick()
        #pedestrian.apply_control(control)
        #spectator.set_transform(get_transform(vehicle.get_location(), vehicle.get_transform().rotation))
        #spectator.set_transform(vehicle.get_transform())
        spectator.set_transform(get_transform(pedestrian.get_location(), 90))
        #spectator.set_transform(pedestrian.get_transform())
        time.sleep(0.02)

    walkerControllerActor.stop()

    carla.command.DestroyActor(walkerControllerActor)

    client.apply_batch([carla.command.DestroyActor(x) for x in vehicles_list])
    client.apply_batch([carla.command.DestroyActor(x) for x in ped_list])
    




  


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("\ndone.")