import requests
import json
import time
import calendar


def ggzy(url,i,timebegin,timeend):
    # url = 'http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp?TIMEBEGIN_SHOW=2019-01-02&TIMEEND_SHOW=2019-01-02&TIMEBEGIN=2019-01-02&TIMEEND=2019-01-02&DEAL_TIME=06&DEAL_CLASSIFY=01&DEAL_STAGE=0100&DEAL_PROVINCE=0&DEAL_CITY=0&DEAL_PLATFORM=0&DEAL_TRADE=0&isShowAll=1&PAGENUMBER=1&FINDTXT=&validationCode='
    rep = requests.get(url)
    content = rep.json()
    print(content)
    print(content["ttlpage"])
    print("数量",content["ttlrow"])
    output = {
        "cata":i,
        "pages":content["ttlpage"],
        "nums":content["ttlrow"],
        "timebegin":timebegin,
        "timeend":timeend
    }
    return output


if __name__ == '__main__':
    # timebegin = '2019-01-02'
    # timeend = '2019-01-02'
    DEAL_STAGE = ["01", "02", "90"]
    listr = []
    list = []
    year = 2018
    month = 12
    daye = ['2019-01-03',]
    if daye:
        dates = daye
    else:
        days = range(calendar.monthrange(year, month)[1] + 1)[1:]
        for day in days:
            print("{}-{}-{}".format(year, month, day))
            days ="{}-{}-{}".format(year, month, day)
            dates =[]
            dates.append(days)
    for date in dates:
        timebegin = timeend =date

        for i in DEAL_STAGE:
            time.sleep(10)
            url = 'http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp?TIMEBEGIN_SHOW={}&TIMEEND_SHOW={}&TIMEBEGIN={}&TIMEEND={}&DEAL_TIME=06&DEAL_CLASSIFY={}&DEAL_STAGE={}00&DEAL_PROVINCE=0&DEAL_CITY=0&DEAL_PLATFORM=0&DEAL_TRADE=0&isShowAll=1&PAGENUMBER=1&FINDTXT=&validationCode='.format(timebegin,timebegin,timeend,timeend,i,i)

            print(url,i,timebegin,timeend)
            k = ggzy(url,i,timebegin,timeend)
            list.append(k)
        print(json.dumps(list))
        result = json.dumps(list)
        total = 0

    for v in list:
        print(v)
        total += int(v['nums'])
    print(total)
    result  = [{"total":total},list]
    print(json.dumps(result))





