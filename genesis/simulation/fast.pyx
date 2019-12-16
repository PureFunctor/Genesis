#cython: language_level=3

cdef extern from "c_simulation.h":
    int FREQUENCY_MAX

    ctypedef struct SimulationData:
        int sample_size
        int roll_count_aggregate
        int dupe_count_aggregate
        int *roll_count_frequency_array
        int *dupe_count_frequency_array
    
    SimulationData *new_SimulationData(int sample_size);
    void del_SimulationData(SimulationData *simulation_data);
    void simulation(int cc, int tc, SimulationData *simulation_data);
    void collect(int cc, int tc, SimulationData *simulation_data);


def aggregate(int cc, int tc, int sample_size) -> dict:
    """Behaves the same way as the function defined in the slower Python
    implementation provides; but utilizes a simulation algorithm written
    in C."""

    cdef SimulationData *simulation_data = new_SimulationData(sample_size)
    collect(cc, tc, simulation_data)

    cdef double rcm = simulation_data.roll_count_aggregate / sample_size
    cdef double dcm = simulation_data.dupe_count_aggregate / sample_size

    cdef dict rcf = {
        i: simulation_data.roll_count_frequency_array[i]
        for i in range(FREQUENCY_MAX)
        if simulation_data.roll_count_frequency_array[i]
    }

    cdef dict dcf = {
        i: simulation_data.dupe_count_frequency_array[i]
        for i in range(FREQUENCY_MAX)
        if simulation_data.dupe_count_frequency_array[i]
    }

    cdef dict result_data = {
        "rc_mean": rcm,
        "dc_mean": dcm,
        "rc_frequency": rcf,
        "dc_frequency": dcf,
    }

    del_SimulationData(simulation_data)

    return result_data
