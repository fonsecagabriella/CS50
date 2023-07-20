import csv
import itertools
import sys
import copy

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """

    # TO TEST
    #one_gene = {"Harry"}
    #two_genes = {"James"}
    #have_trait = {"Harry", "James"}

    #create a set with all people to perform next two steps
    all_people = set(people.keys())
    #check who has zero genes
    zero_gene = all_people - (one_gene | two_genes)

    # create dic to save probabilities calculations
    prob_people_gene_trait = dict()

    # to start, everyone gets the values from probability distribution
    for person in all_people:
        gene_p, trait_p =  0, 0

        if person in zero_gene:
            gene_p = PROBS["gene"][0]
            if person in have_trait:
                trait_p = PROBS["trait"][0][True]
            else:
                trait_p = PROBS["trait"][0][False]
        elif person in one_gene:
            gene_p = PROBS["gene"][1]
            if person in have_trait:
                trait_p = PROBS["trait"][1][True]
            else:
                trait_p = PROBS["trait"][1][False]
        else:
            gene_p = PROBS["gene"][2]
            if person in have_trait:
                trait_p = PROBS["trait"][2][True]
            else:
                trait_p = PROBS["trait"][2][False]

        #print(person, gene_p, trait_p, gene_p*trait_p)
        prob_people_gene_trait[person] = (gene_p, trait_p)

    #print(prob_people_gene_trait)

    #now check if person is a child, to update their values
    for person in people:

        if (not people[person]["mother"] == None) and (not people[person]["father"]== None):
            #print(prob_people_gene_trait[person])
            person_gene_prob = p_gets_from_father = p_gets_from_mother = None

            #print(person)

            # determine person father and mother and their genes
            mother = people[person]["mother"]
            if mother in zero_gene:
                p_gets_from_mother = PROBS["mutation"] #never gets gene from mother, unless mutation
            elif mother in one_gene:
                p_gets_from_mother = 0.5
            else:
                p_gets_from_mother = 1 - PROBS["mutation"] #always, unless mutation

            father = people[person]["father"]
            if father in zero_gene:
                p_gets_from_father = PROBS["mutation"] #never gets gene from father, unless mutation
            elif father in one_gene:
                p_gets_from_father = 0.5
            else:
                p_gets_from_father = 1 - PROBS["mutation"] #always, unless mutation


            # if person has one gene, either they get it from their mother or their father
            if person in one_gene:
                # person_gene_prob =
                #   gets_from_mother * not_gets_from_father +
                #   not_gets_from_mother + gets_from_father

                #Ps: the \ in the code allows me to  break the line for better legibility
                person_gene_prob = (p_gets_from_mother * (1-p_gets_from_father)) + \
                                        ((1-p_gets_from_mother) * p_gets_from_father)

            # gets from both mother and father
            if person in two_genes:
                person_gene_prob = (p_gets_from_father) * (p_gets_from_mother)

            # does not get from either father or mother
            if person in zero_gene:
                person_gene_prob = (1-p_gets_from_father) * (1-p_gets_from_mother)

            # recover value of trait, so it doesnt update with last used value
            trait_p = prob_people_gene_trait[person][1]
            prob_people_gene_trait[person] = (person_gene_prob, trait_p)


            #print(prob_people_gene_trait[person])
            #print(person, mother, father)
            #print(mother, mother_gene, p_gets_from_mother)
            #print(father, father_gene, p_gets_from_father)

    # now we will calculate probability to return
    # in summary, it is the probability of the whole set of people happen with their own traits and genes

    #probability to return
    probability_return = 1

    for genes, traits in prob_people_gene_trait.values():
        probability_return *= genes * traits


    #print(probability_return)
    return probability_return


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """

    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p

        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p



def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    # each person is a key in prob,
    # if person has a "sub-key"of gene and trait
    for person in probabilities:
        # sum valyes for gene and trait
        gene_scalar = sum(probabilities[person]["gene"].values())
        trait_scalar = sum(probabilities[person]["trait"].values())

        #print(person, gene_scalar, trait_scalar)

        # treat values for gene and trait, so they equal to 1
        gene_scalar = 1 / gene_scalar
        trait_scalar = 1 / trait_scalar

        #update p_copy with  new values
        for key, value in probabilities[person]["gene"].items():
            probabilities[person]["gene"][key] = gene_scalar * probabilities[person]["gene"][key]

        for key, value in probabilities[person]["trait"].items():
            probabilities[person]["trait"][key] = trait_scalar * probabilities[person]["trait"][key]

    #print("Normalise: probabilities")
    #print(probabilities)



if __name__ == "__main__":
    main()
