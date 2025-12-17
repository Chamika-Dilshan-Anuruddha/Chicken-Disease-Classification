import os
from box.exceptions import BoxValueError #type:ignore
from box import ConfigBox #type:ignore
import yaml #type:ignore
from cnnClassifier import logger
import joblib #type:ignore
import json
from pathlib import Path
from typing import Any
import base64

def read_yaml(file_path:Path)-> ConfigBox:
    try:
        with open(file_path, 'r') as f:
            content = yaml.safe_load(f)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


def save_json(file_path:Path, data:dict):
    with open(file_path, 'w') as f:
        json.dump(data, f)


def load_json(file_path:Path)->ConfigBox:
    with open(file_path, 'r') as f:
        content=json.load(f)
    return ConfigBox(content)


def save_bin(file_path:Path, data:Any):
    joblib.dump(data,file_path)


def load_bin(file_path:Path)->Any:
    data=joblib.load(file_path)
    return data


def decodeImage(imgstring:str|bytes, filename:str):
    imgdata=base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImagePath:str)->bytes:
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())


def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.infro(f"Created dirctory at: {path}")


def get_size(file_path:Path)-> str:
    size_in_kb=round(os.path.getsize(file_path)/1024)
    return f" ~{size_in_kb} KB"