import json
import requests


class db_handle:

    def __int__(self, GRANT_TYPE, APP_ID, APP_SECRET):
        self.GRANT_TYPE = GRANT_TYPE
        self.APP_ID = APP_ID
        self.APP_SECRET = APP_SECRET

    # '''获取小程序token'''
    def get_access_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type={0}&appid={1}&secret={2}'.format(
            self.GRANT_TYPE, self.APP_ID, self.APP_SECRET)
        response = requests.get(url)
        result = response.json()
        # print(result)
        return result['access_token']

    # '''新增集合'''
    @staticmethod
    def add_collection(access_token, data):
        url = 'https://api.weixin.qq.com/tcb/databasecollectionadd?access_token={0}'.format(access_token)
        # data = {
        #     "env": "ming-tt86j",
        #     "collection_name": "introduction"
        # }
        # print(type(data))
        data['env'] = 'ming-tt86j'
        response = requests.post(url, data=json.dumps(data))
        print('1.新增集合：' + response.text)

    # '''新增数据'''
    @staticmethod
    def add_data(access_token, query):
        url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token={0}'.format(access_token)
        # query = '''db.collection(\"introduction\").add({
        #             data: [{
        #                 key: "qq",
        #                 value: 12345
        #             }]
        #         })
        #         '''
        # print(query)
        # print(type(query))
        data = {
            "env": "ming-tt86j",
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('2.新增数据：' + response.text)

    # '''查询数据'''
    @staticmethod
    def query_data(access_token):
        url = 'https://api.weixin.qq.com/tcb/databasequery?access_token={0}'.format(access_token)
        query = '''
                 db.collection(\"test_collection\").get()
                '''
        data = {
            "env": "ming-tt86j",
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('3.查询数据：' + response.text)
        result = response.json()
        result_list = (result['data'])
        for i in range(len(result_list)):
            result_value = json.loads(result['data'][i])
            print(result_value)

        # for i in range(len(result_list)):
        #     print(type(result_list[i]))
        #     print(result_list[i])

    # '''删除数据'''
    @staticmethod
    def delete_data(access_token, data_id):
        url = 'https://api.weixin.qq.com/tcb/databasedelete?access_token={0}'.format(access_token)
        query = '''db.collection("test_collection").doc("{0}").remove()'''.format(data_id)

        data = {
            "env": "ming-tt86j",
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('4.删除数据：' + response.text)
