# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random

# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    user_agent_ip_list = [
        "http://122.96.59.102:81",
        "http://14.18.238.177:4040",
        "http://144.112.91.97:90",
        "http://124.202.169.54:8118"
       ]
    def process_request(self, request, spider):
        # Set the location of the proxy
        proxy_ip = random.choice(self.user_agent_ip_list)
        request.meta['proxy'] = "123.456.789.10:8888"

        # Use the following lines if your proxy requires authentication
        proxy_user_pass = "awesome:dude"
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
