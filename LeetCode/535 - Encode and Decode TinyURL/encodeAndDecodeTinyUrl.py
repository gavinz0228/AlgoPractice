class Codec:
    def __init__(self):
        self.counter = 0
        self.num_url = {}
        self.url_num = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.counter += 1
        self.url_num[longUrl] = self.counter
        self.num_url[self.counter] = longUrl
        return "http://tinyurl.com/"+ str(self.counter)
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        parts = shortUrl.split('/')
        return self.num_url[int(parts[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))