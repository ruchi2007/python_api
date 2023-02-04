from requests_oauthlib import OAuth1

url_fa = 'http://localhost:8888/rose/wp-json/wc/v3/customers'
update_url_fa= 'http://localhost:8888/rose/wp-json/wc/v3/customers/2'
delete_url_fa= 'http://localhost:8888/rose/wp-json/wc/v3/customers/3?force=true'
auth_fa = OAuth1('ck_22bd8f5a8766395e0fb1ccf68ded616f7deec563', 'cs_27f23bcfda851936b7fa2f93f77699ccc045c47c')

url_op = 'http://localhost:8888/optimum/wp-json/wc/v3/customers'
update_url_op = 'http://localhost:8888/optimum/wp-json/wc/v3/customers/5'
delete_url_op = 'http://localhost:8888/optimum/wp-json/wc/v3/customers/3?force=true'
auth_op = OAuth1('ck_53d693e068ce9b011ed628de89a83693022c7156 ', 'cs_636bbbf7c608fb9d4c67fe605b3b5e95ab11c3c3')