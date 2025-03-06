import multiprocessing
import time

def task(input_data):
    # Simulate some work
    return input_data * 2

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5]
    
    start_time = time.time()
    
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(task, input_list)
    
    end_time = time.time()
    
    latency = end_time - start_time
    
    print(f"Results: {results}")
    print(f"Latency: {latency:.4f} seconds")