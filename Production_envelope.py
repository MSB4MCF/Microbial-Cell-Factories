def production_envelope(model, target_rxn, biomass_rxn, n_pts=20, plot=True):
    """Byproduct secretion envelope (mirrors RAVEN runProductionEnvelope).
    Returns (biomass_values, target_lower, target_upper)."""
    m = model.copy()
    m.objective = biomass_rxn
    growth_max = m.slim_optimize()
    m.objective_direction = 'min'
    growth_min = m.slim_optimize()

    biomass_values = np.linspace(growth_min, growth_max, n_pts)
    lower = np.full(n_pts, np.nan)
    upper = np.full(n_pts, np.nan)

    m.objective = target_rxn
    br = m.reactions.get_by_id(biomass_rxn)
    for i, bv in enumerate(biomass_values):
        br.bounds = (bv, bv)               # fix growth rate
        m.objective_direction = 'max'
        upper[i] = m.slim_optimize()
        m.objective_direction = 'min'
        lower[i] = m.slim_optimize()

    if plot:
        plt.figure(figsize=(6, 4))
        plt.plot(np.concatenate([biomass_values, biomass_values[::-1]]),
                 np.concatenate([upper, lower[::-1]]), 'b', linewidth=2)
        plt.xlabel('Growth rate (1/h)')
        plt.ylabel(target_rxn.replace('_', '-') + ' (mmol/gDW h)')
        plt.title('Production envelope')
        plt.tight_layout()
        plt.show()
    return biomass_values, lower, upper
