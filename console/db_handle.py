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
        print('0.新增集合：' + response.text)

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
        print('1.新增数据：' + response.text)

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
        print('3.删除数据：' + response.text)

    # '''修改数据'''
    @staticmethod
    def modify_data(access_token, query):
        url = 'https://api.weixin.qq.com/tcb/databaseupdate?access_token={0}'.format(access_token)
        # query = ''''''
        data = {
            "env": "ming-tt86j",
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('4.修改数据：' + response.text)

    # '''查询数据'''
    @staticmethod
    def query_data(access_token, query):
        url = 'https://api.weixin.qq.com/tcb/databasequery?access_token={0}'.format(access_token)
        # query = '''
        #          db.collection(\"introduction\").limit(100).get()
        #         '''
        data = {
            "env": "ming-tt86j",
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('5.查询数据：' + response.text)
        result = response.json()
        # print(type(result))
        # print(result)
        result_list = (result['data'])
        # print(type(result_list))
        # print(result_list)
        for i in range(len(result_list)):
            result_value = json.loads(result['data'][i])
            print(result_value)
        return result_list

    # '''查询单条数据'''
    @staticmethod
    def query_data_one(access_token, query):
        url = 'https://api.weixin.qq.com/tcb/databasequery?access_token={0}'.format(access_token)
        # query = '''
        #          db.collection(\"introduction\").limit(100).get()
        #         '''
        data = {
            "env": "ming-tt86j",
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('5.查询数据：' + response.text)
        result = response.json()
        result_list = (result['data'])
        return result_list

    @staticmethod
    def query_result_handle(query_response):
        query_response = query_response[0]
        query_response = query_response.split(',')
        # print(query_response)
        # print(len(query_response))
        query_result = []
        for i in range(len(query_response)):
            element = query_response[i].split(':')
            element = element[1].replace('"', '')
            # print(element)
            query_result.append(element)
        return query_result

    @staticmethod
    def question_Single(query_result):
        query_return = [query_result[3], query_result[4], query_result[5], query_result[6], query_result[7],
                        query_result[9], query_result[10]]
        return query_return

    @staticmethod
    def question_multiple(query_result):
        query_return = [query_result[3], query_result[4], query_result[5], query_result[6], query_result[7],
                        query_result[9], query_result[10]]
        return query_return

    @staticmethod
    def question_judge(query_result):
        query_return = [query_result[3], query_result[4], query_result[5], query_result[7], query_result[8]]
        return query_return

    @staticmethod
    def question_read_before(query_result):
        query_return = [query_result[3], query_result[5]]
        return query_return

    @staticmethod
    def mind_think(query_result):
        query_return = [query_result[1], query_result[3], query_result[5], query_result[6], query_result[7],
                        query_result[8], query_result[9]]
        return query_return

    @staticmethod
    def words_sentence(query_result):
        query_result[6] = query_result[6].replace('}', '')
        query_return = [query_result[3], query_result[6]]
        return query_return