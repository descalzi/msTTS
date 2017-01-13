#!/usr/bin/python3

###
import http.client
import urllib.parse
import json

###############################
# Microsoft Speech API service
class msTTS(object):
    """
    Microsoft Speech API service
    """

    ###############################
    def __init__(self, api_key, file_type='mp3', lang='en-GB', voice='Female'):
        """
        Initialize MSFT Cognitive Services Speech API
        """

        api_key = "62ca8030261f4889b9a48520dfe36b63"
        self.api_key = api_key

        self.file_type = 'mp3'
        self.language = 'en-GB'
        self.voice = 'Female'

        self.http_params = ""
        self.http_headers = {"Ocp-Apim-Subscription-Key": apiKey}

        self.http_AccessTokenHost = "api.cognitive.microsoft.com"
        self.path = "/sts/v1.0/issueToken"
        self.status = False


    ###############################
    def get_token(self):
        """
        Connect and get token for TTS request
        """

        # Connect to server to get the Access Token
        conn = http.client.HTTPSConnection(self.http_AccessTokenHost)


        conn.request("POST", self.http_path, self.http_params, self.http_headers)
        response = conn.getresponse()

        if (response.status == 200):
            data = response.read()
            self.status = True
        else:
            self.status = False

        conn.close()

        self.accesstoken = data.decode("UTF-8")

        return self.status

    ###############################
    def get_tts_file(self, phrase='', language='en-GB', voice='Female', file_type='mp3'):

        if (file_type):
            self.file_type = file_type
        if (language):
            self.language = language
        if (voice):
            self.voice = voice

        valid_voice = {}
        valid_voice['en-GB']= {}
        valid_voice['en-GB']['Female'] = 'George'
        valid_voice['en-GB']['Male'] = 'George'

        if (self.file_type == 'mp3')
            output_format = 'riff-16khz-16bit-mono-pcm'
        elif (self.file_type == 'wav'):
            output_format = 'audio-16khz-32kbitrate-mono-mp3'

        body = "<speak version='1.0' xml:lang='en-us'><voice xml:lang='"+self.language+"' xml:gender='"+self.voice+"' name='Microsoft Server Speech Text to Speech Voice ("+self.language+", "+valid_voice[self.language][self.voice]+", Apollo)'>"+phrase+"</voice></speak>"

        headers = {"Content-type": "application/ssml+xml",
                    "X-Microsoft-OutputFormat": ""+output_format+"",
                    "Authorization": "Bearer " + self.accesstoken,
                    "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
                    "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
                    "User-Agent": "TTSForPython"}

        #Connect to server to synthesize the wave
        print ("Connect to server to synthesize the wave")
        #python2> conn = httplib.HTTPSConnection("speech.platform.bing.com")
        conn = http.client.HTTPSConnection("speech.platform.bing.com")
        conn.request("POST", "/synthesize", body, headers)
        response = conn.getresponse()
        print ("Got wave response")
        print (response.status, response.reason)

        data = response.read()
        conn.close()
        print ("The synthesized wave length: %d" %(len(data)))

        print ("Saving synthesized wave file: %s" %('/tmp/msft_tts.mp3'))
        file_wav = open('/tmp/msft_tts.mp3', 'wb')
        file_wav.write(data)
