import recognition_process as rp
from multiprocessing import Process, Queue

recognition_results_queue = Queue()

def main():
    p = Process(target=rp.speech_recognition_process,
                 args=(rp.recognizer, recognition_results_queue),
                   daemon=True)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCaught Ctrl + C. Exiting")

