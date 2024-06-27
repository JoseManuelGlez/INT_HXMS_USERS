import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from infrastructure.controllers import api_rest

if __name__ == "__main__":
    api_rest.start_api()