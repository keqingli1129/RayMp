import ray

# Initialize Ray
ray.init(num_gpus=0)

@ray.remote
def square(x):
    return x * x

# Launch tasks in parallel
futures = [square.remote(i) for i in range(10)]
results = ray.get(futures)

print("Squares:", results)

# Shutdown Ray
ray.shutdown()