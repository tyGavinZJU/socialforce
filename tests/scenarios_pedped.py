import numpy as np
import socialforce
import random
import logging

def test_crossing():
    log = logging.getLogger('test_crossing')
    agentNum = 30
    state = []
    for episode in range(10):
        for num in range(agentNum):
            
            v1 = random.uniform(-0.5,0.5)
            v2 = random.uniform(-0.5,0.5)

            p1 = random.uniform(0,10)
            p2 = random.uniform(0,10)
            p3 = random.uniform(0,10)
            p4 = random.uniform(0,10)

            p = [p1,p2,v1,v2,p3,p4]
            if num == 0:
                state = np.array([p])
            else:
                state = np.append(state,[p],0)

        log.debug(state)
        print('hello')
        
        initial_state2 = np.array([
            [0.0, 0.0, 0.5, 0.5, 10.0, 10.0],
            [10.0, 0.3, 0.5, 0.5, 0.0, 10.0],
        ])
        
        
        initial_state = np.array(state)
        print('state:',state)
        print('initial state:',initial_state)
        print('initial state2:',initial_state2)
        s = socialforce.Simulator(initial_state)
        states = np.stack([s.step().state.copy() for _ in range(50)])

        # visualize
        print('')
        filename = 'crossing'+str(episode)+'.png'
        with socialforce.show.canvas('docs/cross/'+filename) as ax:
            ax.set_xlabel('x [m]')
            ax.set_ylabel('y [m]')

            for ped in range(agentNum):
                x = states[:, ped, 0]
                y = states[:, ped, 1]
                #ax.plot(x, y, '-o', label='ped {}'.format(ped), markersize=2.5)
                ax.plot(x, y, '-o',  markersize=2.5)
            ax.legend()


def test_narrow_crossing():
    initial_state = np.array([
        [0.0, 0.0, 0.5, 0.5, 2.0, 10.0],
        [2.0, 0.3, -0.5, 0.5, 0.0, 10.0],
    ])
    s = socialforce.Simulator(initial_state)
    states = np.stack([s.step().state.copy() for _ in range(40)])

    # visualize
    print('')
    with socialforce.show.canvas('docs/narrow_crossing.png') as ax:
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')

        for ped in range(2):
            x = states[:, ped, 0]
            y = states[:, ped, 1]
            ax.plot(x, y, '-o', label='ped {}'.format(ped), markersize=2.5)
        ax.legend()


def test_opposing():
    initial_state = np.array([
        [0.0, 0.0, 1.0, 0.0, 0.0, 10.0],
        [-0.3, 10.0, -1.0, 0.0, -0.3, 0.0],
    ])
    s = socialforce.Simulator(initial_state)
    states = np.stack([s.step().state.copy() for _ in range(21)])

    # visualize
    print('')
    with socialforce.show.canvas('docs/opposing.png') as ax:
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')

        for ped in range(2):
            x = states[:, ped, 0]
            y = states[:, ped, 1]
            ax.plot(x, y, '-o', label='ped {}'.format(ped), markersize=2.5)
        ax.legend()


def test_2opposing():
    initial_state = np.array([
        [0.0, 0.0, 0.5, 0.0, 0.0, 10.0],
        [0.6, 10.0, -0.5, 0.0, 0.6, 0.0],
        [2.0, 10.0, -0.5, 0.0, 2.0, 0.0],
    ])
    s = socialforce.Simulator(initial_state)
    states = np.stack([s.step().state.copy() for _ in range(40)])

    # visualize
    print('')
    with socialforce.show.canvas('docs/2opposing.png') as ax:
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')

        for ped in range(3):
            x = states[:, ped, 0]
            y = states[:, ped, 1]
            ax.plot(x, y, '-o', label='ped {}'.format(ped), markersize=2.5)
        ax.legend()

