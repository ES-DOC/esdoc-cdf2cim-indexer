import dramatiq



# Queue to which messages will be dispatched.
_QUEUE = "cmip6.simulations"



@dramatiq.actor(queue_name=_QUEUE)
def process_simulation(institute, source_id, experiment):
    print(f"{institute}, {source_id}, {experiment}")
