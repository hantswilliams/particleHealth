#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:11:37 2021

@author: hantswilliams



"""





import requests 



######### Step 1 - Generate JWT 

particleid = "INSERTHERE"
particlesecret = "INSERTHERE"

endpointauth = 'https://sandbox.particlehealth.com/auth'
particleheaders = {'client-id': particleid, 'client-secret': particlesecret}

particleresponse = requests.get(endpointauth, headers=particleheaders)


particleresponse.status_code
jwtresponse = particleresponse.text

print(particleresponse)


############# Step 2 - Make a basic GET request to pull down data 

endpointmetadata = 'https://sandbox.particlehealth.com/R4/metadata'

headerswithjwt = {"Content-Type": "application/json", 
           'Authorization': jwtresponse}

responsemeta = requests.get(endpointmetadata, headers=headerswithjwt)
responsemeta.status_code

responsemetaText = responsemeta.text
responsemetaJson = responsemeta.json()


test = pd.DataFrame(responsemetaJson['rest'][0]['resource'])



########### Step 3 - Make a basic GET request to pull down patient data 

url = 'https://sandbox.particlehealth.com/R4/Encounter/?person={person_id}'

newResponse = requests.get(url, headers=headerswithjwt)
newResponse.status_code
newResponseJson = newResponse.json()










