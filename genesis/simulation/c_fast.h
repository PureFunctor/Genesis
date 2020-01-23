#ifndef C_FAST_H
#define C_FAST_H

extern int FREQUENCY_MAX;

typedef struct _SimulationData {

    int sample_size;
    int roll_count_agg;
    int dupe_count_agg;
    int *roll_count_frq;
    int *dupe_count_frq;

} SimulationData;

SimulationData *new_SimulationData(int sample_size);
void del_SimulationData(SimulationData *simulation_data);

void c_simulate(int cc, int tc, SimulationData *simulation_data);
void c_aggregate(int cc, int tc, SimulationData *simulation_data);

#endif
