import re
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests

jobplanet_id = "kimx2966@umn.edu"
jobplanet_pw = "cjswo3670"
login_url = 'https://www.jobplanet.co.kr/users/sign_in'


comp_lst = []
# user_lst = []
dept_lst = []
titl_lst = []
dat1_lst = []
diff_lst = []
dat2_lst = []
rout_lst = []
head_lst = []
mask_lst = []
took_lst = []
fell_lst = []
ress_lst = []
good_lst = []

###
total_lst = []
###

class web:
	def __init__(self, soup, company):
		self.company = company
		self.comp_lst = []
		self.user_lst = []
		self.dept_lst = []
		self.titl_lst = []
		self.dat1_lst = []
		self.diff_lst = []
		self.dat2_lst = []
		self.rout_lst = []
		self.head_lst = []
		self.mask_lst = []
		self.took_lst = []
		self.fell_lst = []
		self.ress_lst = []
		self.good_lst = []

	# 웹 데이터 정제 함수
	def who_clean(self, i):
	    '''
	    작성자 정보 출력시 시행하는 데이터 클린
	    '''
	    clean = re.sub('[\n\n\n\xa0/\xa0\n|\n\n\n\n]',"",i.text)
	    return clean.split()

	def remove_tag(self, i):
	    clear = re.compile("<.*?>")
	    text = re.sub(clear, '', str(i))
	    return text
	    
	def rout_clean(self, i):
	    '''
	    면접 난이도 관련 데이터 추출시 시행하는 데이터 클린
	    '''
	    clean = re.sub('[\n          ]',"",i)
	    return clean
	    
	def label_clean(self, i):
	    '''
	    작성자의 헤드라인 정보 출력시 시행하는 데이터 클린
	    '''
	    clean = re.sub('[\n\n]',"",str(i))
	    clean = re.sub('\r','. ',clean)
	    clean = re.sub('            ',"",clean)
	    clean = re.sub('          ',"",clean)
	    return clean

	    
	def question_clean(self, i):
	    cle = re.sub('[\n\r2]',"",str(i))
	    cle = ' '.join(cle.split())
	    return cle

	def result_clean(self, i):
	    clean = re.sub('[\n\n]',"",i)
	    clean = re.sub('[              ]',"",clean)

	    return clean

	
	# 웹 데이터 전처리
	def company_info(self, company):
		self.comp_lst.append(str(company))

	# def clean_user(self, i):
	#     # user_id = i['data-content_id']    
	#     who = i.find_all('div',{'class':'content_top_ty2'})
	#     dept = self.remove_tag(who).split()[1]
	#     titl = self.remove_tag(who).split()[3]
	#     dat1 = self.remove_tag(who).split()[5]

	#     # self.user_lst.append(user_id)
	#     self.dept_lst.append(dept)
	#     self.titl_lst.append(titl)
	#     self.dat1_lst.append(dat1)

	def clean_user(self, i):
	    # user_id = i['data-content_id']    
		who = i.find_all('div',{'class':'content_top_ty2'})
		# splt = self.remove_tag(who).split()
		try:
			dept = self.remove_tag(who).split()[1]
			titl = self.remove_tag(who).split()[3]
			dat1 = self.remove_tag(who).split()[5]
		except IndexError:
			dept = None
			titl = None
			dat1 = None
	    
	    # self.user_lst.append(user_id)
		self.dept_lst.append(dept)
		self.titl_lst.append(titl)
		self.dat1_lst.append(dat1)


	def clean_difficulty(self, i):
	    diff = i.find('span','blo_txt2')
	    if diff == None:
	        self.diff_lst.append(None)
	    else:
	        diff = diff.text
	        self.diff_lst.append(diff)
	        
	    dat2 = i.find('dd', 'txt1')#.text
	    if dat2 == None:
	        self.dat2_lst.append(None)
	    else:
	        dat2 = dat2.text
	        self.dat2_lst.append(dat2)

	    rout = i.find('dd', 'txt2')
	    if rout == None:
	        self.rout_lst.append(rout)
	    else:
	        rout = self.remove_tag(self.rout_clean(str(rout)))
	        self.rout_lst.append(rout)
	        
	def clean_headline(self, i):
	    head = i.find_all('h2',{'class':'us_label'})
	    head = self.remove_tag(self.label_clean(head))
	    head = head[2:-2]
	    self.head_lst.append(head)

	def clean_interview(self, i):
	    ques = i.find_all('dl',{'class':'tc_list'})
	    ### main question
	    for i, num1 in zip(ques, range(0,1)):
	        mask = i.find('span').text
	        mask = self.question_clean(mask)
	        self.mask_lst.append(mask)
	        if num1 == 0:
	            break
	    ### thought
	    for i, num2 in zip(ques, range(0,1)):
	        fell = i.find_all('span', 'answer')
	        fell = self.remove_tag(fell)
	        if len(fell) <= 2:
	            fell = None
	            self.fell_lst.append(fell)
	        else:
	            fell = self.question_clean(fell)
	            fell = fell[1:-2]
	            self.fell_lst.append(fell)
	        if num2 == 0:
	            break
	    ### 기간
	    for i, num3 in zip(ques, range(0,1)):
	        took = self.remove_tag(i)
	        took = str(took).split('일')[0]
	        took = took[-2:]
	        try:
	            took = int(took)
	            self.took_lst.append(took)
	        except ValueError:
	            took = None
	            self.took_lst.append(took)
	        if num3 == 0:
	            break
	            
	def clean_exprience(self, i):
	    expr = i.find_all('dd',"txt_img")
	    expr = self.result_clean(self.remove_tag(expr))
	    expr = expr.split(',')
	    ress = expr[0][1:]
	    good = expr[1][:-1]

	    self.ress_lst.append(ress)
	    self.good_lst.append(good)

	# Web Crawling
	def crawl(self, soup, company):
		# first_check = soup.find_all("span",{'class':'txt2'})
		
		# check = [str(i).split()[2][:4] for i in first_check]

		single = soup.select('section')
		for i in single:
		# 	if year == '2019':
			try:
				self.clean_interview(i)
				self.clean_exprience(i)
				self.company_info(company)
				self.clean_user(i)
				self.clean_difficulty(i)
				self.clean_headline(i)
			except (KeyError, IndexError, AttributeError):
				break
			# else:
			# 	break





