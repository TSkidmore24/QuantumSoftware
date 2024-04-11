def compute_average_values(bs: BitString, G: nx.Graph, T: float):
    #k = 1.38064852 * math.pow(10, -23)
    k=1
    beta = 1 / (k * T)
    energy_and_mag_values = []
    possible_configs = 2 ** len(bs)
    Z = 0.0

    # Compute energies and magnetizations for all configurations
    for index in range(possible_configs):
        bs.set_int_config(index)
        en = energy(bs, G)
        m = bs.on() - bs.off()
        energy_and_mag_values.append((en, m))
        Z += math.exp(-beta * en)

    # Calculate probabilities and average values
    E = 0.0
    M = 0.0
    M_squared = 0.0
    E_squared = 0.0
    for energy_of_config, mag_of_config in energy_and_mag_values:
        prob_of_config = math.exp(-beta * energy_of_config) / Z
        weighted_energy = prob_of_config * energy_of_config
        weighted_mag = prob_of_config * mag_of_config
        M_squared += prob_of_config * mag_of_config**2
        E_squared += prob_of_config * energy_of_config**2
        E += weighted_energy
        M += weighted_mag

    # Additional calculations for heat capacity and magnetic susceptibility
    HC = (1/T**2) * (E_squared - E**2)
    MS = (1/T) * (M_squared - M**2)

    return E, M, HC, MS
