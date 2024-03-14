import numpy as np
import random
from main import next_state, Alive

def test_next_state():
    state = np.zeros((100, 100), dtype=object)
    agent_list = [
        Alive(x=50, y=50),
        Alive(x=40, y=60),
        Alive(x=70, y=70),
        Alive(x=10, y=30),
        Alive(x=20, y=20),
        Alive(x=80, y=80),
        Alive(x=30, y=70),
        Alive(x=60, y=40)
    ]

    # Run the function
    out_state = next_state(state, agent_list)

    # Assertions
    assert out_state.shape == (100, 100)
    assert isinstance(out_state[50][50], Alive)
    assert isinstance(out_state[40][60], int)  # Died
    assert isinstance(out_state[70][70], Alive)
    assert isinstance(out_state[10][30], int)  # Died
    assert isinstance(out_state[20][20], Alive)
    assert isinstance(out_state[80][80], Alive)
    assert isinstance(out_state[30][70], Alive)
    assert isinstance(out_state[60][40], Alive)
    assert out_state[50][50].positionX != 50 or out_state[50][50].positionY != 50  # Agent has moved

    print("All test cases passed.")

# Run the test cases
test_next_state()
