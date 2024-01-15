# 1.0 Getting the list of UCSC genomes - First try

#"requests" is a python library that allows you to make HTTP requests
import requests
# To form a request, you will need a base URL (which will take you to the right
# Table Browser of UCSC and then a set of parameters which will tell the
# browser API what information you are after
# Set the base URL to use the Table Browser
base_url = "https://api.genome.ucsc.edu/list/ucscGenomes"

response = requests.get(base_url)
print(response.text)


#1.1put the format into json - easier to read
import requests
import json

base_url = "https://api.genome.ucsc.edu/list/ucscGenomes"

response = requests.get(base_url)

print(json.dumps(json.loads(response.text), indent=4))

#using parameters in an api request
base_url = "https://api.genome.ucsc.edu/getData/sequence"

# Set the parameters for the request
params = {
        'genome': 'hg38',
        'chrom' : 'chr7',
        'start': '117480025',
        'end': '117668665'
        }

response = requests.get(base_url, params= params) #don't forget to include params in response!

print(json.dumps(json.loads(response.text), indent=4))


#2.0 using api documentation to list tracks for a certain genome
import requests, sys

base_url = "https://api.genome.ucsc.edu/list/tracks"
params = {
    'genome': 'hg38',
        }
response = requests.get(base_url, params=params)
print(json.dumps(json.loads(response.text), indent=3))

#3.0Searching for the sequence of the CFTR transcript ENST00000003084.11 (chr7:117480025-117668665 )
#This time we will use a base_url with the words getData?sequence in it.

base_url = "https://api.genome.ucsc.edu/getData/sequence"
params = {
        'genome': 'hg38',
        'chrom' : 'chr7',
        'start': '117480025',
        'end': '117668665'
        }
response = requests.get(base_url, params=params)
print(json.dumps(json.loads(response.text), indent=3))


#3.1:  Retrieving all data from a track for a specific genomic region
#      Here, we need to use a base_url with the words getData?track .

base_url = "https://api.genome.ucsc.edu/getData/track"
params = {
        'genome': 'hg38',
        'track' : 'snp150',
        'chrom' : 'chr7',
        'start': '117480025',
        'end': '117668665'
    }
response = requests.get(base_url, params=params)
print(json.dumps(json.loads(response.text), indent=3))








