from enum import Enum
from schema.schemas import *

class SchemaEnum(Enum):
    PATIENTS = (patients_schema, "patients.csv")
    EXERCISES = (exercises_schema, "exercises.csv")
    STEPS = (steps_schema, "steps.csv")

    def __init__(self, schema, file_path):
        self.schema = schema
        self.file_path = file_path

    @classmethod
    def get_schema(cls, name: str):
        try:
            return cls[name.upper()].schema
        except KeyError:
            raise ValueError(f"Schema {name} not found")

    @classmethod
    def get_file_path(cls, name: str):
        try:
            return cls[name.upper()].file_path
        except KeyError:
            raise ValueError(f"File path for schema {name} not found")

    