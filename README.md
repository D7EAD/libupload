<h1 align="center">libupload</h1></center>
<p align="center">A Python library to upload files--easily.</p>
<hr>
libupload is a Python library that allows users to seamlessly upload files to remote upload sites within their programs without having to deal with all the HTTP(S) nonsense.
<br><br>
As of now, there are only three APIs in libupload--AnonFile, BayFiles, and File.io. Their identifiers can be found below:

```
  API_ANONFILE = 0x0
  API_BAYFILES = 0x1
  API_FILE_IO = 0x2
```

<br><br>
Files can be uploaded very easily within programs. You can find an example below:

```
def main():
  u = Uploader()
  pathToFile = "path here"
  u.sendFiles(API_ANONFILE, pathToFile)
```

<br><br>
The URLs to access your uploaded files will be stored in the object's `url` member and can be accessed like so:

```
def main():
  u = Uploader()
  pathToFile = "path here"
  u.sendFiles(API_ANONFILE, pathToFile)
  print(u.url)
```

```
Output:
  https://anonfiles.com/NaV9dwaCap9
```
