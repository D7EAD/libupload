import json
import requests
import os

# C-style enum values for error identification
ERROR_FILE_NO_EXIST = 0x0
ERROR_FILE_FAIL_UPLOAD = 0x1

# dictionary to hold error strings for exception class
errors = ["Given file does not exist!", "File failed to upload!"]

# Exception class
class LUException(Exception):
    pass

# C-style enum values for API identifiers
API_ANONFILE = 0x0
API_BAYFILES = 0x1
API_FILE_IO = 0x2

class Uploader():
    def __init__(self, timeout=(5, 5)):
        self.response = None
        self.url = None
        self.status = None
        self.timeout = timeout

#    @func: __checkFileExistence(self, filePath)
#    @brief
#       Internal function for checking if given files exist.
#       Used before uploading a file; checks given file.
#    @return
#       Returns True if file exists.
#       Raises LUException code 0x00 if file not found.
    def __checkFileExistence(self, filePath):
        if (os.path.exists(filePath)):
            return True
        else:
            raise LUException(errors[ERROR_FILE_NO_EXIST])

#    @func: prepareFile(self, api, filePath)
#    @brief
#       Prepares a file for upload to the chosen API.
#    @return None
    def sendFile(self, api, filePath):
        if (self.__checkFileExistence(filePath)):
            self.__uploadFile(api, filePath)

#    @func: uploadFile(self, api, filePath)
#    @brief
#       Uploads a file to the given API internally.
#       If successful, returns values into respective class members.
#       If fails, raises LUException code 0x01.
    def __uploadFile(self, api, filePath):
        try: 
            file = {'file': open(filePath, 'rb')}
            if (api == API_ANONFILE):
                res = requests.post("https://api.anonfiles.com/upload", files=file, verify=True, timeout=self.timeout)
                self.status = bool(res.json()['status'])
                self.response = res.json()
                self.url = res.json()['data']['file']['url']['short']
                if (self.status != True):
                    raise LUException(errors[ERROR_FILE_FAIL_UPLOAD])
            elif (api == API_BAYFILES):
                res = requests.post("https://api.bayfiles.com/upload", files=file, verify=True, timeout=self.timeout)
                self.status = bool(res.json()['status'])
                self.response = res.json()
                self.url = res.json()['data']['file']['url']['short']
                if (self.status != True):
                    raise LUException(errors[ERROR_FILE_FAIL_UPLOAD])
            elif (api == API_FILE_IO):
                res = requests.post("https://file.io/", files=file, verify=True, timeout=self.timeout)
                self.status = bool(res.json()['success'])
                self.response = res.json()
                self.url = res.json()['link']
                if (self.status != True):
                    raise LUException(errors[ERROR_FILE_FAIL_UPLOAD])
        except Exception as e:
            raise LUException(str(e))