#!/usr/bin/python3
from models.engine import file_storage
import models.base_model


class_dict = {"BaseModel":base_model.BaseModel}
storage = file_storage.FileStorage()
storage.reload()
