
import time
import multiprocessing

def main():
    for i in range(100000000000000000):
        print(i)
        time.sleep(1)

if __name__ == '__main__':        
    p = multiprocessing.Process(target=main,name='main')
    p.start()
    time.sleep(10)
    p.terminate()
    p.join()
