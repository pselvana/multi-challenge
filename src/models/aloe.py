from src.models.base import ModelProvider
import os
from typing import List, Dict


class AloeModel(ModelProvider):
    AloeEndpoint = "https://staging.aloe.inc"

    def __init__(self):
        print("Initialized Aloe model")

        #create new tenant on Aloe; tenant should have no customizations for user profile
        self.init = True

    def generate(self, chat: List[Dict]) -> str:
        """Generate a response from the model."""
        # Parse pairs of user system calls to seed Aloe with
        # Aloe should produce "thoughts" via pulse for pairs

        # Aloe should be polled to ensure that all pulses are complete

        # Finally call Aloe with last user request and await response


        # Debug
 
        return "Aloe says: Success!"
