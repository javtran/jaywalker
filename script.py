import carla
import random

from lib import SimulationVisualization, MapNames, MapManager, Simulator

SpawnActor = carla.command.SpawnActor

def main():
    
    # CONNECT CLIENT TO SERVER
    print(f"connecting to remote: 127.0.0.1:2000")
    client = carla.Client("127.0.0.1",2000)
    client.set_timeout(10.0)
    print(f"connected to remote: 127.0.0.1:2000")

    # GETTING THE MAPMANAGER AND LOADING MAP
    mapManager = MapManager(client)
    mapManager.load(MapNames.circle_t_junctions)

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
    
    results = client.apply_batch_sync(batch_ped, True)

    # SPAWN CARS
    car_spawn_points = mapManager.spawn_points
    batch_car = list()
    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_global_distance_to_leading_vehicle(2.5)
    SetAutopilot = carla.command.SetAutopilot
    FutureActor = carla.command.FutureActor
    for i in range(5):
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
            vehicles_list.aapend(i.actor_id)

    # CAMERA
    camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
    camera_bp.set_attribute('image_size_x', str(1000))
    camera_bp.set_attribute('image_size_y', str(562))
    camera = world.spawn_actor(camera_bp, spectator.get_transform(), attach_to = vehicles_list[0])
    


    onTickers = [visualizer.onTick]
    onEnders = []
    simulator = Simulator(client, onTickers=onTickers, onEnders=onEnders)
    simulator.run(1000)


    spectator = world.get_actors()
    print(spectator)




  


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("\ndone.")