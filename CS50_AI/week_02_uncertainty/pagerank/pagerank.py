import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000

def main_test():
    corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
    page = "2.html"
    damping_factor = 0.85

    print(sample_pagerank(corpus, damping_factor, 100))

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.

    example:
    corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
    page = 1.html
    damping_factor = 0.85

    transition_model = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}

    """

    # get outgoing links for a page as a key
    sub_corpus = list(corpus[page])

    transition_model = {} #initiate transition model to return


    if len(sub_corpus) > 0: # if the page has outgoing links
        #calculates the extra value for each page
        extra_value = (1 - damping_factor) / (len(sub_corpus))
        extra_value = format(extra_value, ".3f")
        # calculates the value of damping factor for each following page
        prob_value = damping_factor / len(sub_corpus)
        prob_value = format(prob_value, ".3f") # format to 3 digits

        #updates pagerank of page
        #transition_model[page] = float(extra_value) #converts the value to float to comply with assignment

        #update pagerank of children - outgoing links
        #for p in sub_corpus:
        #    transition_model[p] = float(prob_value) #converts the value to float to comply with assignment


        for p in corpus:
            if p not in sub_corpus and not p==page:
                #updates pagerank of page that is not outgoing link
                transition_model[p] = float(extra_value)
            else:
                #update pagerank of children - outgoing links
                transition_model[p] = float(extra_value) +float(prob_value)


    else:
        # if a page has no links, we can pretend it has links to all pages in the corpus,
        # including itself
        prob_value =  1/len(corpus)
        prob_value = format(prob_value, ".3f")

        for key, value in corpus.items():
            transition_model[key] = float(prob_value)

    return transition_model

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.


    """
    page_rank =  {}

    #initiate the page rank with available keys, and value 0
    for page in corpus:
        page_rank[page] = 0

    # generate random start
    parent_page = random.choice(list(page_rank.keys()))

    # initiate loop count
    i =0


    while i < n:

        #the next sample should be generated from the previous sample
        # based on the previous sample’s transition model.
        parent_tm = transition_model(corpus, parent_page, damping_factor)

        # from the TM above, select one random child page by
        # using transition model as weight
        child_page = random.choices(list(parent_tm.keys()),
                                        weights=list(parent_tm.values()))[0]

        #updates page_rank with the number of times page was visited
        page_rank[parent_page] += 1

        #updates value of parent page
        parent_page = child_page

        # increments i count
        i += 1

    #Normalises the values by /n
    for p in page_rank:
        #attention to formatting to comply with assignment
        n_value = page_rank[p]/n
        n_value = format(n_value, ".3f")
        page_rank[p] = float(n_value)

    #print("\nSUM SAMPLING")
    #print(sum(page_rank.values()))

    return page_rank


    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Dictionary to store pagerank
    pagerank = {}

    # Iterate over all pages and assign initial probability to pagerank
    for page in corpus:
        pagerank[page] = 1 / len(corpus)

    # Keep boolean to know when the results start converging (difference no greater than 0.001)
    converged = False
    while not converged:
        # Copy pagerank
        pagerank_copy = {k: v for k, v in pagerank.items()}
        # Keep difference to find out whether results converge and we can stop
        pagerank_diff = {}

        # Iterate over each page in corpus
        for page in corpus.keys():
            # Keep count of current pagerank
            probability = 0

            # Summation: PR(i) / NumLinks(i)
            for page_i, pages in corpus.items():
                # Check if current page has a link to our page p
                if page in pages:
                    # Use previous pagerank for summation
                    probability += pagerank_copy[page_i] / len(pages)
                # In case current page has no links to other pages
                elif len(pages) == 0:
                    # Interpret as having one link for every page
                    probability += 1 / len(corpus)

            # Calculate the rest of the formula given in task background for iterative algorithm
            pagerank[page] = (1 - damping_factor) / len(corpus) + (damping_factor * probability)

            # Store the difference between previous pagerank and current to know when to stop
            pagerank_diff[page] = abs(pagerank_copy[page] - pagerank[page])
            # print(pagerank_diff)

        # Check if we can leave the while loop by making sure if there is no gap of more than 0.001 between
        # current pagerank and previous pagerank
        converged = True
        for page in pagerank_diff:
            if pagerank_diff[page] > 0.001:
                converged = False

    # Important: normalize.
    # Pageranks must sum up to 1. In case with corpus2, they do not sum up and thus need to be normalized
    # by dividing each pagerank with their overall sum
    sum_pagerank = 0
    for k in pagerank:
        sum_pagerank += pagerank[k]

    for k in pagerank:
        pagerank[k] = pagerank[k] / sum_pagerank


    print("\nSUM ITERATIVE")
    print(sum(pagerank.values()))

    return pagerank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {}

    #print("CORPUS")
    #print(corpus)

    #The function should begin by assigning each page a rank of 1 / N,
    # where N is the total number of pages in the corpus
    total_pages = len(corpus)
    for p in corpus:
        page_rank[p] = 1/total_pages

    #The function should then repeatedly calculate new rank values based
    # on all of the current rank values,
    # according to the PageRank formula in the “Background” section.
    # (i.e., calculating a page’s PageRank based on the PageRanks of
    # all pages that link to it).


    #first condition
    #it’s 1 - d divided by N, where N is the total number of pages across the entire corpus
    pr_fc =  ((1 - damping_factor) / total_pages )


    # we will create a loop for the second condition
    # the loop will stop when all the values of pagerank[p] are < 0.001
    pr_sc = None

    # first I will save all childs and their parents in a dic
    # in this dict, if I have "A" : {P1, P2} it means that P1 and P2 have links to A
    child_parents = {}


    for child in corpus.keys():
        # ads p to child_parents dic as a key
        child_parents[child] = []

        #look for pages that are a parent of page child
        for parent in corpus:

            if child in corpus[parent]: #if c
                child_parents[child].append(parent)

    loop = True

    while loop==True:

        loop = False #set the loop to false, to avoid running forever
                    #loop will start again based on checking differences of page rank

        # create a copy of page rank for comparing values
        start_page_rank = copy.deepcopy(page_rank)

        '''TESTS
        print("PAGERANK")
        print(page_rank)
        print(start_page_rank)
        print("\n\n")
        print("CORPUS")
        print(corpus) '''

        # loop through all the pages - keys, in corpus
        for p in corpus.keys():
            #initiate second condition before gets in loop
            pr_sc = 0

            #calculate second part of the formula

            #based on the parents of page p
            for p_i in child_parents[p]:
                if not len(corpus[p_i]) == 0:
                    pr_sc += start_page_rank[p_i] / len(corpus[p_i])
                else:
                    pr_sc += 1 / total_pages

            #apply dampening factor to second part of formula
            pr_sc = pr_sc * damping_factor

            #finally calculates PR
            page_rank[p] =  pr_fc + pr_sc


            #print("TEST - PAGERANK UPDATED PAGE")
            #print(page_rank[p])
            #print("\n\n")

        #check if any page rank (old-new > 0.001, if so, start loop again)
        for s in start_page_rank:
            if abs(page_rank[s] - start_page_rank[s]) > 0.001:
                loop= True

    #Normalises the values by /n
    # first create n, this needs to be assigned here, before going into loop to avoid issues
    n = sum(page_rank.values())
    for p in page_rank:
        #attention to formatting to comply with assignment
        pr_value = page_rank[p]/n
        pr_value = format(pr_value, ".3f")
        page_rank[p] = float(pr_value)

    #print("SUM ITERATION")
    #print(n)
    #print(sum(page_rank.values()))
    return page_rank

if __name__ == "__main__":
    main()
