import pkg_resources
import random
import sys
import warnings

from packaging import version

import pandas as pd

try:
    from src.util.functions import log_msg

except (ImportError, ModuleNotFoundError) as error:
    print(error)
    print(sys.exc_info())
    pass


# * Setup
pd.options.mode.chained_assignment = None  # default="warn"


def assert_library_versions() -> None:
    """ Asserts key library versions
    """
    try:
        assert version.parse(pd.__version__) >= version.parse("1.2.4"), (f"Currently installed Pandas version is {pd.__version__}.")
    except:
        print(f"\nPython version:\t{sys.version}\n")
        print(
            f"\nLibrary versions:\n"
            f"   Pandas:\t{pd.__version__}\n"
        )


def set_seeds(seed: int = 6020, ) -> None:
    """ Set random seeds for all libraries.

    Args:
        seed (int, optional): Random seed integer. Defaults to 6020.
    """
    #np.random.seed(seed)
    #random.seed(seed)
    # tf.set_random_seed(seed)
    # torch.seed(seed)
    #torch.manual_seed(seed)
    #torch.cuda.manual_seed(seed)


def activate_plotly_in_notebook() -> None:
    """ VSC requires to set plotly's render default to 'plotly_mimetype+notebook'.
    """
    if pio.renderers.default in ["databricks", "plotly_mimetype+notebook"]:
        log_msg(f"Plotly default render prior:\t{pio.renderers.default}.")
    else:
        log_msg(f"Plotly default render prior:\t{pio.renderers.default}.")
        pio.renderers.default = "plotly_mimetype+notebook"
        log_msg(f"Plotly default render post:\t{pio.renderers.default}.")
