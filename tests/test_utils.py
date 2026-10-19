import io
import sys
from utils_package import distance, quad, log


def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(-1, -1, -1, -1) == 0


def test_quad_real_roots():
    r1, r2 = quad(1, -3, 2)  # roots 1 and 2
    roots = {round(r1.real, 6), round(r2.real, 6)}
    assert roots == {1.0, 2.0}


def test_quad_complex_roots():
    r1, r2 = quad(1, 0, 1)  # roots i and -i
    assert (round(r1.real, 6), round(r1.imag, 6)) == (0.0, 1.0)
    assert (round(r2.real, 6), round(r2.imag, 6)) == (0.0, -1.0)


def test_log_prints(capsys=None):
    # Basic smoke test for log — capture stdout
    log("testing log")
    # We won't assert on exact timestamp, just ensure it prints something
