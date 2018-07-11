# @Author: cherong 
# @Date: 2018-07-10 16:13:10 
# @Last Modified by:   cherong 
# @Last Modified time: 2018-07-10 16:13:10 
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            print(res.status_code)
        return res.json()
        
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header).json()
        else:
            res = requests.get(url=url,data=data).json()
        return res
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == "post":
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        