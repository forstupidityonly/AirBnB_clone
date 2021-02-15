#!/usr/bin/python3
from models.engine import file_storage
import models.base_model
import models.user
import models.state
import models.city
import models.amenity
import models.place
import models.review


class_dict = {"BaseModel": base_model.BaseModel, "User": user.User,
              "Place": place.Place, "City": city.City, "State": state.State,
              "Amenity": amenity.Amenity, "Review": review.Review}
storage = file_storage.FileStorage()
storage.reload()
