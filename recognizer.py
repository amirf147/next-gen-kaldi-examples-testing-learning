#!/usr/bin/env python3

# This script is based on the example file copied from https://github.com/k2-fsa/sherpa-onnx/blob/master/python-api-examples/speech-recognition-from-microphone.py

from pathlib import Path

import sherpa_onnx


TOKENS = "./models/sherpa-onnx-streaming-zipformer-en-2023-06-26/tokens.txt"
ENCODER = "./models/sherpa-onnx-streaming-zipformer-en-2023-06-26/encoder-epoch-99-avg-1-chunk-16-left-128.onnx"
DECODER = "./models/sherpa-onnx-streaming-zipformer-en-2023-06-26/decoder-epoch-99-avg-1-chunk-16-left-128.onnx"
JOINER = "./models/sherpa-onnx-streaming-zipformer-en-2023-06-26/joiner-epoch-99-avg-1-chunk-16-left-128.onnx"

def assert_file_exists(filename: str):
    assert Path(filename).is_file(), (
        f"{filename} does not exist!\n"
        "Please refer to "
        "https://k2-fsa.github.io/sherpa/onnx/pretrained_models/index.html to download it"
    )

assert_file_exists(ENCODER)
assert_file_exists(DECODER)
assert_file_exists(JOINER)
assert_file_exists(TOKENS)

recognizer = sherpa_onnx.OnlineRecognizer.from_transducer(
    tokens=TOKENS,
    encoder=ENCODER,
    decoder=DECODER,
    joiner=JOINER,
    num_threads=1,
    sample_rate=16000,
    feature_dim=80,
)
