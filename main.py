import recognition_process as rp

def main():
    rp.speech_recognition_process(rp.recognizer)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCaught Ctrl + C. Exiting")
