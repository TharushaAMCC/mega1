import requests

payload = {"Authorization":"JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1YzNkYjU0M2E2MWE1NTA1MjQxZWU4YzciLCJtb2JpbGUiOiI3NjMzNzI1MjYiLCJrZXkiOiI1NDI5Njk5IiwiaWF0IjoxNjA1OTYzMDcwfQ.6isj1TU3LJ5PaHySpTFxiHWpTrlDW2iBzvTGzeuXiSI","X-Unity-Version":"2018.3.0f2","Host":"http://megarun.dialog.lk"}
r = requests.post("https://megarun.dialog.lk/api/v2/play", data=payload)
print(r.text)
