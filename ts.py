import  sqlite3
machine0 =r'''D:\TESTSpiderResult.db3'''
sql = '''INSERT into "ggzy"(cata,pages,nums,timebegin,timeend)
VALUES({},{},{},{},{}) '''
# format(i['cata'],i['pages'],i['nums'],i['timebegin'],i['timeend'])
list = [{"cata": "01", "pages": 7009, "nums": 140166, "timebegin": "2018-12-1", "timeend": "2018-12-1"}, {"cata": "02", "pages": 7254, "nums": 145077, "timebegin": "2018-12-1", "timeend": "2018-12-1"}, {"cata": "90", "pages": 42457, "nums": 849127, "timebegin": "2018-12-1", "timeend": "2018-12-1"}, {"cata": "01", "pages": 7008, "nums": 140152, "timebegin": "2018-12-2", "timeend": "2018-12-2"}, {"cata": "02", "pages": 7255, "nums": 145090, "timebegin": "2018-12-2", "timeend": "2018-12-2"}, {"cata": "90", "pages": 42457, "nums": 849139, "timebegin": "2018-12-2", "timeend": "2018-12-2"}, {"cata": "01", "pages": 7009, "nums": 140174, "timebegin": "2018-12-3", "timeend": "2018-12-3"}, {"cata": "02", "pages": 7254, "nums": 145077, "timebegin": "2018-12-3", "timeend": "2018-12-3"}, {"cata": "90", "pages": 42458, "nums": 849153, "timebegin": "2018-12-3", "timeend": "2018-12-3"}, {"cata": "01", "pages": 7009, "nums": 140180, "timebegin": "2018-12-4", "timeend": "2018-12-4"}, {"cata": "02", "pages": 7254, "nums": 145077, "timebegin": "2018-12-4", "timeend": "2018-12-4"}, {"cata": "90", "pages": 42457, "nums": 849139, "timebegin": "2018-12-4", "timeend": "2018-12-4"}, {"cata": "01", "pages": 7009, "nums": 140167, "timebegin": "2018-12-5", "timeend": "2018-12-5"}, {"cata": "02", "pages": 7255, "nums": 145100, "timebegin": "2018-12-5", "timeend": "2018-12-5"}, {"cata": "90", "pages": 42458, "nums": 849153, "timebegin": "2018-12-5", "timeend": "2018-12-5"}, {"cata": "01", "pages": 7009, "nums": 140167, "timebegin": "2018-12-6", "timeend": "2018-12-6"}, {"cata": "02", "pages": 7254, "nums": 145077, "timebegin": "2018-12-6", "timeend": "2018-12-6"}, {"cata": "90", "pages": 42460, "nums": 849194, "timebegin": "2018-12-6", "timeend": "2018-12-6"}, {"cata": "01", "pages": 7011, "nums": 140204, "timebegin": "2018-12-7", "timeend": "2018-12-7"}, {"cata": "02", "pages": 7257, "nums": 145124, "timebegin": "2018-12-7", "timeend": "2018-12-7"}, {"cata": "90", "pages": 42461, "nums": 849204, "timebegin": "2018-12-7", "timeend": "2018-12-7"}, {"cata": "01", "pages": 7011, "nums": 140204, "timebegin": "2018-12-8", "timeend": "2018-12-8"}, {"cata": "02", "pages": 7257, "nums": 145130, "timebegin": "2018-12-8", "timeend": "2018-12-8"}, {"cata": "90", "pages": 42461, "nums": 849204, "timebegin": "2018-12-8", "timeend": "2018-12-8"}, {"cata": "01", "pages": 7011, "nums": 140204, "timebegin": "2018-12-9", "timeend": "2018-12-9"}, {"cata": "02", "pages": 7257, "nums": 145130, "timebegin": "2018-12-9", "timeend": "2018-12-9"}, {"cata": "90", "pages": 42461, "nums": 849204, "timebegin": "2018-12-9", "timeend": "2018-12-9"}, {"cata": "01", "pages": 7011, "nums": 140204, "timebegin": "2018-12-10", "timeend": "2018-12-10"}, {"cata": "02", "pages": 7257, "nums": 145129, "timebegin": "2018-12-10", "timeend": "2018-12-10"}, {"cata": "90", "pages": 42457, "nums": 849140, "timebegin": "2018-12-10", "timeend": "2018-12-10"}, {"cata": "01", "pages": 7011, "nums": 140208, "timebegin": "2018-12-11", "timeend": "2018-12-11"}, {"cata": "02", "pages": 7258, "nums": 145147, "timebegin": "2018-12-11", "timeend": "2018-12-11"}, {"cata": "90", "pages": 42461, "nums": 849208, "timebegin": "2018-12-11", "timeend": "2018-12-11"}, {"cata": "01", "pages": 7011, "nums": 140218, "timebegin": "2018-12-12", "timeend": "2018-12-12"}, {"cata": "02", "pages": 7257, "nums": 145139, "timebegin": "2018-12-12", "timeend": "2018-12-12"}, {"cata": "90", "pages": 42462, "nums": 849222, "timebegin": "2018-12-12", "timeend": "2018-12-12"}, {"cata": "01", "pages": 7011, "nums": 140218, "timebegin": "2018-12-13", "timeend": "2018-12-13"}, {"cata": "02", "pages": 7257, "nums": 145139, "timebegin": "2018-12-13", "timeend": "2018-12-13"}, {"cata": "90", "pages": 42463, "nums": 849243, "timebegin": "2018-12-13", "timeend": "2018-12-13"}, {"cata": "01", "pages": 7011, "nums": 140211, "timebegin": "2018-12-14", "timeend": "2018-12-14"}, {"cata": "02", "pages": 7258, "nums": 145147, "timebegin": "2018-12-14", "timeend": "2018-12-14"}, {"cata": "90", "pages": 42463, "nums": 849243, "timebegin": "2018-12-14", "timeend": "2018-12-14"}, {"cata": "01", "pages": 7011, "nums": 140218, "timebegin": "2018-12-15", "timeend": "2018-12-15"}, {"cata": "02", "pages": 7258, "nums": 145144, "timebegin": "2018-12-15", "timeend": "2018-12-15"}, {"cata": "90", "pages": 42464, "nums": 849267, "timebegin": "2018-12-15", "timeend": "2018-12-15"}, {"cata": "01", "pages": 7014, "nums": 140266, "timebegin": "2018-12-16", "timeend": "2018-12-16"}, {"cata": "02", "pages": 7262, "nums": 145233, "timebegin": "2018-12-16", "timeend": "2018-12-16"}, {"cata": "90", "pages": 42464, "nums": 849261, "timebegin": "2018-12-16", "timeend": "2018-12-16"}, {"cata": "01", "pages": 7019, "nums": 140361, "timebegin": "2018-12-17", "timeend": "2018-12-17"}, {"cata": "02", "pages": 7264, "nums": 145271, "timebegin": "2018-12-17", "timeend": "2018-12-17"}, {"cata": "90", "pages": 42464, "nums": 849261, "timebegin": "2018-12-17", "timeend": "2018-12-17"}, {"cata": "01", "pages": 7019, "nums": 140362, "timebegin": "2018-12-18", "timeend": "2018-12-18"}, {"cata": "02", "pages": 7265, "nums": 145284, "timebegin": "2018-12-18", "timeend": "2018-12-18"}, {"cata": "90", "pages": 42466, "nums": 849310, "timebegin": "2018-12-18", "timeend": "2018-12-18"}, {"cata": "01", "pages": 7019, "nums": 140365, "timebegin": "2018-12-19", "timeend": "2018-12-19"}, {"cata": "02", "pages": 7265, "nums": 145287, "timebegin": "2018-12-19", "timeend": "2018-12-19"}, {"cata": "90", "pages": 42464, "nums": 849261, "timebegin": "2018-12-19", "timeend": "2018-12-19"}, {"cata": "01", "pages": 7019, "nums": 140370, "timebegin": "2018-12-20", "timeend": "2018-12-20"}, {"cata": "02", "pages": 7265, "nums": 145284, "timebegin": "2018-12-20", "timeend": "2018-12-20"}, {"cata": "90", "pages": 42466, "nums": 849310, "timebegin": "2018-12-20", "timeend": "2018-12-20"}, {"cata": "01", "pages": 7019, "nums": 140369, "timebegin": "2018-12-21", "timeend": "2018-12-21"}, {"cata": "02", "pages": 7265, "nums": 145287, "timebegin": "2018-12-21", "timeend": "2018-12-21"}, {"cata": "90", "pages": 42464, "nums": 849261, "timebegin": "2018-12-21", "timeend": "2018-12-21"}, {"cata": "01", "pages": 7019, "nums": 140369, "timebegin": "2018-12-22", "timeend": "2018-12-22"}, {"cata": "02", "pages": 7265, "nums": 145284, "timebegin": "2018-12-22", "timeend": "2018-12-22"}, {"cata": "90", "pages": 42466, "nums": 849310, "timebegin": "2018-12-22", "timeend": "2018-12-22"}, {"cata": "01", "pages": 7019, "nums": 140369, "timebegin": "2018-12-23", "timeend": "2018-12-23"}, {"cata": "02", "pages": 7265, "nums": 145287, "timebegin": "2018-12-23", "timeend": "2018-12-23"}, {"cata": "90", "pages": 42466, "nums": 849310, "timebegin": "2018-12-23", "timeend": "2018-12-23"}, {"cata": "01", "pages": 7019, "nums": 140378, "timebegin": "2018-12-24", "timeend": "2018-12-24"}, {"cata": "02", "pages": 7265, "nums": 145294, "timebegin": "2018-12-24", "timeend": "2018-12-24"}, {"cata": "90", "pages": 42479, "nums": 849565, "timebegin": "2018-12-24", "timeend": "2018-12-24"}, {"cata": "01", "pages": 7023, "nums": 140443, "timebegin": "2018-12-25", "timeend": "2018-12-25"}, {"cata": "02", "pages": 7261, "nums": 145219, "timebegin": "2018-12-25", "timeend": "2018-12-25"}, {"cata": "90", "pages": 42489, "nums": 849766, "timebegin": "2018-12-25", "timeend": "2018-12-25"}, {"cata": "01", "pages": 7023, "nums": 140444, "timebegin": "2018-12-26", "timeend": "2018-12-26"}, {"cata": "02", "pages": 7267, "nums": 145333, "timebegin": "2018-12-26", "timeend": "2018-12-26"}, {"cata": "90", "pages": 42489, "nums": 849775, "timebegin": "2018-12-26", "timeend": "2018-12-26"}, {"cata": "01", "pages": 7023, "nums": 140444, "timebegin": "2018-12-27", "timeend": "2018-12-27"}, {"cata": "02", "pages": 7267, "nums": 145333, "timebegin": "2018-12-27", "timeend": "2018-12-27"}, {"cata": "90", "pages": 42489, "nums": 849766, "timebegin": "2018-12-27", "timeend": "2018-12-27"}, {"cata": "01", "pages": 7023, "nums": 140443, "timebegin": "2018-12-28", "timeend": "2018-12-28"}, {"cata": "02", "pages": 7267, "nums": 145333, "timebegin": "2018-12-28", "timeend": "2018-12-28"}, {"cata": "90", "pages": 42476, "nums": 849513, "timebegin": "2018-12-28", "timeend": "2018-12-28"}, {"cata": "01", "pages": 7023, "nums": 140444, "timebegin": "2018-12-29", "timeend": "2018-12-29"}, {"cata": "02", "pages": 7267, "nums": 145333, "timebegin": "2018-12-29", "timeend": "2018-12-29"}, {"cata": "90", "pages": 42495, "nums": 849898, "timebegin": "2018-12-29", "timeend": "2018-12-29"}, {"cata": "01", "pages": 7023, "nums": 140455, "timebegin": "2018-12-30", "timeend": "2018-12-30"}, {"cata": "02", "pages": 7269, "nums": 145380, "timebegin": "2018-12-30", "timeend": "2018-12-30"}, {"cata": "90", "pages": 42489, "nums": 849780, "timebegin": "2018-12-30", "timeend": "2018-12-30"}, {"cata": "01", "pages": 7025, "nums": 140494, "timebegin": "2018-12-31", "timeend": "2018-12-31"}, {"cata": "02", "pages": 7271, "nums": 145404, "timebegin": "2018-12-31", "timeend": "2018-12-31"}, {"cata": "90", "pages": 42518, "nums": 850353, "timebegin": "2018-12-31", "timeend": "2018-12-31"}]
k = 0
for i in list:
    k+=i['nums']
print(k)

