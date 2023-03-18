# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)] 
    for i in range(m):
        t = data[i]
        thread_id, time_finished = min(threads, key=lambda x: x[1])
        output.append((thread_id, time_finished))
        threads[thread_id] = (thread_id, time_finished + t)
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    #result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_id, start_time in result:
        print(thread_id, start_time)

if __name__ == "__main__":
    main()
