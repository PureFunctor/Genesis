#include <stdlib.h>
#include <time.h>
#include "c_simulation.h"

int FREQUENCY_MAX = 512;

SimulationData *new_SimulationData(int sample_size)
{
    SimulationData *simulation_data = malloc(sizeof(SimulationData));

    simulation_data->sample_size = sample_size;
    simulation_data->roll_count_aggregate = 0;
    simulation_data->dupe_count_aggregate = 0;
    simulation_data->roll_count_frequency_array = calloc(FREQUENCY_MAX, sizeof(int));
    simulation_data->dupe_count_frequency_array = calloc(FREQUENCY_MAX, sizeof(int));

    return simulation_data;   
}

void del_SimulationData(SimulationData *simulation_data)
{
    free(simulation_data->roll_count_frequency_array);
    free(simulation_data->dupe_count_frequency_array);
    free(simulation_data);
}

void simulation(int cc, int tc, SimulationData *simulation_data)
{
    int i = 0;
    int f = 0;

    int roll_count = 0;
    int dupe_count = 0;

    int generation_power = 0;
    int draws_count = 0;
    int zeros_count = 0;

    int *owned = calloc(cc, sizeof(int));
    int *zeros = calloc(cc, sizeof(int));
    int *drawn = calloc(5,  sizeof(int));

    tc = cc >= tc ? tc : cc;

    while (!f) {
        roll_count++;
        draws_count = generation_power < 100 ? 5 : 4;

        for (i = 0; i < draws_count; i++) {
            drawn[i] = rand() % cc;
        }

        if (draws_count == 4) {
            zeros_count = 0;
            for (i = 0; i < cc; i++) {
                if (!owned[i]) {
                    zeros[zeros_count++] = i;
                }
            }
            drawn[4] = zeros[rand() % zeros_count];
            generation_power = 0;
        }

        for (i = 0; i < 5; i++) {
            if (owned[drawn[i]]++) {
                dupe_count++;
                generation_power += 10;
            }
        }
        
        f = 1;
        for (i = 0; i < tc; i++) {
            if (!owned[i]) {
                f = 0;
            }
        }
    }

    free(owned);
    free(zeros);
    free(drawn);

    simulation_data->roll_count_aggregate += roll_count;
    simulation_data->dupe_count_aggregate += dupe_count;
    simulation_data->roll_count_frequency_array[roll_count]++;
    simulation_data->dupe_count_frequency_array[dupe_count]++;
}

void collect(int cc, int tc, SimulationData *simulation_data)
{
    int i;

    srand(time(0));

    for (i = 0; i < simulation_data->sample_size; i++) {
        simulation(cc, tc, simulation_data);
    }
}
