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
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        raise e


def load_json(file_path:Path)->ConfigBox:
    try:
        with open(file_path, 'r') as f:
            content=json.load(f)
        return ConfigBox(content)
    except Exception as e:
        raise e


def save_bin(file_path:Path, data:Any):
    try:
        joblib.dump(data,file_path)
    except Exception as e:
        raise e


def load_bin(file_path:Path)->Any:
    try:
        data=joblib.load(file_path)
        return data
    except Exception as e:
        raise e


def decodeImage(imgstring:str|bytes, filename:str):
    try:
        imgdata=base64.b64decode(imgstring)
        with open(filename, 'wb') as f:
            f.write(imgdata)
    except Exception as e:
        raise e


def encodeImageIntoBase64(croppedImagePath:str)->bytes:
    try:
        with open(croppedImagePath, 'rb') as f:
            return base64.b64encode(f.read())
    except Exception as e:
        raise e


def create_directories(path_to_directories:list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created dirctory at: {path}")
    except Exception as e:
        raise e


def get_size(file_path:Path)-> str:
    try:
        size_in_kb=round(os.path.getsize(file_path)/1024)
        return f" ~{size_in_kb} KB"
    except Exception as e:
        raise e