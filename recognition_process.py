from recognizer import recognizer
from audio_input import sd 
import queue as queue_module

def speech_recognition_process(recognizer, queue):

    # The model is using 16 kHz, we use 48 kHz here to demonstrate that
    # sherpa-onnx will do resampling inside.
    sample_rate = 48000
    samples_per_read = int(0.1 * sample_rate)  # 0.1 second = 100 ms
    last_result = ""
    stream = recognizer.create_stream()
    
    with sd.InputStream(channels=1, dtype="float32", samplerate=sample_rate) as s:
        while True:
            samples, _ = s.read(samples_per_read)  # a blocking read
            samples = samples.reshape(-1)
            stream.accept_waveform(sample_rate, samples)
            while recognizer.is_ready(stream):
                recognizer.decode_stream(stream)
            result = recognizer.get_result(stream)
            
            if last_result != result:
                last_result = result
                # print("\r{}".format(result), end="\n", flush=True)
                
                # Check if q has elements
                if not queue.empty():
                    print("Queue is not empty! Something is in it.")
                
                try:
                    latest_item = queue.get(block=False) 
                    print("Latest item in queue:", latest_item)
                except queue_module.Empty:
                    pass # Ignore if queue is empty

                print("Queue size:", queue.qsize())
                queue.put(result, block=False)
