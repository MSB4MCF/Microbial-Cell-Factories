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

