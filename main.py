import requests
import json

class Cloudflare_DNS(object):
    def __init__(self, zone, email, api_key, dns_type, dns_name, content, delete_id):
        self.dns_type = dns_type
        self.dns_name = dns_name
        self.zone = zone
        self.email = email
        self.api_key = api_key
        self.content = content
        self.delete_id = delete_id
        self.url = 'https://api.cloudflare.com/client/v4/zones/' + self.zone + '/dns_records'
        self.headers = {'Content-Type': 'application/json', 'X-Auth-Key': self.api_key, 'X-Auth-Email': self.email}


    def create_record(self):
        self.payload = {'type': self.dns_type, 'name': self.dns_name, 'content': self.content}
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        json_data = json.loads(r.text)
        try:
            if json_data["result"]["id"]:
                print "success"
                # I store the ID in a database so that I can retrieve it later when I want to delete it
        except:
            print "fail"
        print json_data

    def delete_record(self):
        r = requests.delete(self.url + '/' + self.delete_id, headers=self.headers)
        json_data = json.loads(r.text)
        if json_data["success"] == True:
            print "success"
        else:
            print "fail"
        print json_data
