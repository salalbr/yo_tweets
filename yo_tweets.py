from commandr import command, Run
from twitter import *


@command('search', category='Search')
def DoSearch(query, cred, since=None, until=None):
  """Search tweets matching search qeury
  Arguments:
    query - search query.
    since - lower bound date/time limit.
    since - upper bound date/time limit.
    
  """
  print('Query: {}'.format(query))

  # Read credentials file
  config = {}
  execfile(cred, config)

  # Connect to Twitter API
  twitter = connect_to_twitter_api(config)

  # Fire query to API endpoint
  query = twitter.search.tweets(**compose_query_params(q=query, since=since, until=until))

  # Show results
  print('Search complete: {:.3f} seconds'.format(query["search_metadata"]["completed_in"]))
  for result in query["statuses"]:
    print('({0}) @{1} {2}'.format(
      str(result["created_at"]),
      str(result["user"]["screen_name"]),
      str(result["text"].encode('utf-8'))
    ))

def compose_query_params(**kwargs):
  params = {}
  for key, value in kwargs.iteritems():
    if value:
      params[key] = value
  return params

def connect_to_twitter_api(config):
  return Twitter(
    auth = OAuth(
      config["access_key"],
      config["access_secret"],
      config["consumer_key"],
      config["consumer_secret"]
    )
  )


if __name__ == '__main__':
  Run()
