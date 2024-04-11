def energy(bs: BitString, G: nx.Graph):
    """Compute energy of configuration, `bs`

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : Graph
        input graph defining the Hamiltonian
    Returns
    -------
    energy  : float
        Energy of the input configuration
    """
    energy = 0.0
    for edge in G.edges():
        i, j = edge
        si = 1
        if bs.config[i] == 0:
            si = -1
        sj = 1
        if bs.config[j] == 0:
            sj = -1
        energy += G.edges[edge]['weight'] * si * sj
    return energy