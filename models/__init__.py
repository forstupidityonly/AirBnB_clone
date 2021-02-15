#!/usr/bin/python3
from models.engine import file_storage
import models.base_model
import models.user

class_dict = {"BaseModel": base_model.BaseModel, "User": user.User}
storage = file_storage.FileStorage()
storage.reload()
