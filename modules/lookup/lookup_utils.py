import googlesearch
from modules.lookup import lookup_constants


def search_query(original_query, target_site="google"):
    """
    Command to search the interwebs! (google)
    """
    if target_site in lookup_constants.REGISTERED_SITES:
        target_site = lookup_constants.REGISTERED_SITES[target_site]
    # If we do a google search, we want to return the 10 top results
    # Otherwise, we want to just send the most relevant result

    # Don't add google to the query but add any other target site for easier access/SEO
    if target_site == lookup_constants.GOOGLE:
        query = original_query
    else:
        query = original_query + " " + target_site

    # Dude this loop is going to be horrible wtf
    # If google:
    #   Store all results as a list and print them out line by line in an embed
    # If not google:
    #   Find the first result that matches the target site and return that
    #   If we can't find it, return the google query I think
    results = []
    for result in googlesearch.search(
        query,
        num_results=lookup_constants.QUERY_NUM,
        sleep_interval=lookup_constants.PAUSE_TIME,
    ):
        if target_site in result:
            return [result]
        results.append(result)

    return results
