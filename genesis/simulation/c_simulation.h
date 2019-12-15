#ifndef C_SIMULATION_H
#define C_SIMULATION_H

extern int FREQUENCY_MAX;

typedef struct _SimulationData {
    int sample_size;
    int roll_count_aggregate;
    int dupe_count_aggregate;
    int *roll_count_frequency_array;
    int *dupe_count_frequency_array;
} SimulationData;

SimulationData *new_SimulationData(int sample_size);
void del_SimulationData(SimulationData *simulation_data);
void simulation(int cc, int tc, SimulationData *simulation_data);
void collect(int cc, int tc, SimulationData *simulation_data);

#endif
