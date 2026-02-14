import platform
from utils.logger import log

def generate_report():
    system = platform.system()
    node = platform.node()

    print("System:", system)
    print("Node:", node)

    log(f"Generated system report for {node}")
