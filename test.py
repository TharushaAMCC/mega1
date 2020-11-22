except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests
    header = {"Host": "megarun.dialog.lk",
              "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1YzNkYjU0M2E2MWE1NTA1MjQxZWU4YzciLCJtb2JpbGUiOiI3NjMzNzI1MjYiLCJrZXkiOiI1NDI5Njk5IiwiaWF0IjoxNjA1OTYzMDcwfQ.6isj1TU3LJ5PaHySpTFxiHWpTrlDW2iBzvTGzeuXiSI", "X-Unity-Version": "2018.3.0f2"}
r = requests.post(url, headers=headers)
