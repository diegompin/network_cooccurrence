import sys
import numpy as np
import networkx as nx
from network_cooccurrence import NetworkCoOccurrence


def main(path_occurrence_network, min_subjects, min_occurrences):
    occurrences = np.genfromtxt(path_occurrence_network, delimiter=',')

    component = NetworkCoOccurrence()

    C, CC, RR_graph, RR_dist, G_rr, Phi_graph, Phi_dist, G_phi = component.get_network(occurrences, min_subjects,
                                                                                       min_occurrences)

    nx.write_graphml(G_phi, 'G_phi.graphml')
    nx.write_graphml(G_rr, 'G_RR.graphml')


if __name__ == '__main__':
    path_occurrence_network = 'occurrence-network.csv'
    min_subjects = 1
    min_occurrences = 1

    if len(sys.argv) > 1:
        path_occurrence_network = sys.argv[1]

    if len(sys.argv) > 2:
        min_subjects = sys.argv[1]
    if len(sys.argv) > 3:
        min_occurrences = sys.argv[1]

    main(path_occurrence_network, min_subjects, min_occurrences)
