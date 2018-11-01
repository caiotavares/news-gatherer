#!/usr/bin/env python3

import json
import os
import html2text
import sys
from requests import request

endpoints = {
  'base': 'https://content.guardianapis.com/',
  'editions': 'https://content.guardianapis.com/editions',
  'international': 'https://content.guardianapis.com/international',
  'search': 'https://content.guardianapis.com/search'
}

def auth_request(method, endpoint_name, path = '', params = {}):
  api_key = os.environ['API_KEY']
  uri = endpoints[endpoint_name] + path
  params.update({'api-key': api_key})
  print('requesting ' + uri)
  response = request(method, uri, params = params)
  return json.loads(response.text)

def extract_content(id):
  response = auth_request('get','base', id, params = {'show-fields': 'body'})
  return response['response']['content']['fields']['body']

def parse_html(html):
  h = html2text.HTML2Text()
  h.ignore_links = True
  return h.handle(html)

def write_to_file(name, content):
  file = open('content/' + name + '.txt', 'w')
  file.write(parse_html(content))
  file.close()

def search(query):
  response = auth_request('get', 'search', params = {'q': query})
  results = list(map(lambda r: r['id'], response['response']['results']))
  if len(results) == 0:
    print('No results were found for ' + query)
  else:
    for r in results:
      content = extract_content(r)
      filename = r.replace('/','-')
      write_to_file(filename, content)
    print('Search results were save to ' + os.curdir + '/content')

if not os.path.exists('content'):
  os.makedirs('content')

argument = sys.argv[1]
search(argument)
