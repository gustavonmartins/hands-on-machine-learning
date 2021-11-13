import pytest

import matplotlib.pyplot as plt


def test_matplotlib_gui():
    """Assert that matplotlib has a GUI backend.
    The error message to avoid is:
    UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure."""
    with pytest.warns(None) as record:
        plt.plot([1, 2, 3, 4])
        plt.ylabel("some numbers")
        plt.show(block=False)
        plt.close()
    assert len(record) == 0
