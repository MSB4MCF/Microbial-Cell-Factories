from cobra import Reaction, Metabolite

def new_rxn(abbreviation, name, lower, upper):
    reaction = Reaction(abbreviation)
    reaction.name = name
    reaction.lower_bound = lower
    reaction.upper_bound = upper
    return reaction

def new_metabolite(abbreviation, Formula, Name, Compartment):
    metabolite = Metabolite(
        abbreviation,
        formula=Formula,
        name=Name,
        compartment=Compartment,
    )
    return metabolite

def extract_metabolite(metabolite_name, model=None):
    target_model = model if model is not None else globals().get("model")
    if target_model is None:
        print("No COBRApy model provided or found in globals.")
        return None
    try:
        return target_model.metabolites.get_by_id(metabolite_name)
    except KeyError:
        print(f"Metabolite '{metabolite_name}' not found in the model")
        return None
