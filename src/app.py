#!/usr/bin/env python3

import json
import os
import html2text
import sys
from requests import request

endpoints = {
  'base': 'https://content.guardianapis.com/',
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

def parse_search_results(response):
  return list(map(lambda r: r['id'], response['response']['results']))

def save_results(results):
  if len(results) == 0:
    print('No results were found')
  else:
    for r in results:
      content = extract_content(r)
      filename = r.replace('/','-')
      write_to_file(filename, content)
    print('Search results were save to ' + os.curdir + '/content')

def write_to_file(name, content):
  file = open('content/' + name + '.txt', 'w')
  file.write(parse_html(content))
  file.close()

def search(query):
  response = auth_request('get', 'search', params = query)
  results = parse_search_results(response)
  save_results(results)

if not os.path.exists('content'):
  os.makedirs('content')

cmd = sys.argv[1]
argument = sys.argv[2]

search({cmd: argument})
