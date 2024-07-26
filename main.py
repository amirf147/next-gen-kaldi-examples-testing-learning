import recognition_process as rp
from multiprocessing import Process, Queue
from queue import Empty
recognition_results_queue = Queue()

def main():

    rp.speech_recognition_process(rp.recognizer, recognition_results_queue)
    
    ########not working
    while True:
        # Check if q has elements
        if not recognition_results_queue.empty():
            print("Queue is not empty! Something is in it.")

        try:
            latest_item = recognition_results_queue.get(block=False) 
            print("Latest item in queue:", latest_item)
        except Empty:
            pass # Ignore if queue is empty

        print("Queue size:", recognition_results_queue.qsize())


    # need to familiarize myself with queue so doing it in the recognition_process.py file
    # and i got something working. i mean i got it into a queue and i can print it from there
    # in that file, that's enough for now, will experiment with bringing here later

    # failed attempts, don't look, definitely don't try, feel free to judge:
    # while True:
    #         try:
    #             recognition_result = recognition_results_queue.get(timeout=1)
    #             print(recognition_result)
    #         except Exception:
    #             print("Queue is empty") 
    # this didn't work because it is nonpicklable
    # p = Process(target=rp.speech_recognition_process,
    #              args=(rp.recognizer, recognition_results_queue),
    #                daemon=True)
    # p.start()
    # p.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCaught Ctrl + C. Exiting")

