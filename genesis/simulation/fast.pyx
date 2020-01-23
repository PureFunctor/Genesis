#cython: language_level=3

cdef extern from "c_fast.h":
    int FREQUENCY_MAX

    ctypedef struct SimulationData:
        int sample_size
        int roll_count_agg
        int dupe_count_agg
        int *roll_count_frq
        int *dupe_count_frq
    
    SimulationData *new_SimulationData(int sample_size);
    void del_SimulationData(SimulationData *simulation_data);

    void c_simulate(int cc, int tc, SimulationData *simulation_data);
    void c_aggregate(int cc, int tc, SimulationData *simulation_data);


def aggregate(int cc, int tc, int sample_size) -> dict:
    cdef SimulationData *simulation_data = new_SimulationData(sample_size)
    c_aggregate(cc, tc, simulation_data)

    cdef double rcm = simulation_data.roll_count_agg / sample_size
    cdef double dcm = simulation_data.dupe_count_agg / sample_size

    cdef dict rcf = {
        i: simulation_data.roll_count_frq[i]
        for i in range(FREQUENCY_MAX)
        if simulation_data.roll_count_frq[i]
    }

    cdef dict dcf = {
        i: simulation_data.dupe_count_frq[i]
        for i in range(FREQUENCY_MAX)
        if simulation_data.dupe_count_frq[i]
    }

    cdef dict result_data = {
        "rc_mean": rcm,
        "dc_mean": dcm,
        "rc_frequency": rcf,
        "dc_frequency": dcf,
    }

    del_SimulationData(simulation_data)

    return result_data
