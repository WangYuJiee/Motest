
"""
    每个接口key为了唯一性保证，在接口名字后面加个请求方式
    1、OPTIONS
    2、HEA
    3、GET
    4、POST
    5、PUT
    6、DELETE
    7、TRACE
    8、CONNECT

    e.g:
       {
       "接口名字&请求方式":["url","请求方式"]}

"""
# 项目地址
# BASE_URL = "http://122.229.8.173:3095"
BASE_URL = "http://192.168.30.154:8899"

sub = '/pyapi'

# 登录注册接口
users = {
    "send_verification_code_email&3": ["/user/send_verification_code_email/{email}", "get"],
    "send_verification_code&3": ["/user/send_verification_code/{phone}", "get"],
    # /user/send_verification_code/{phone}	# get	给手机发送验证码
    "check_username_exist&3": ["/user/check_username_exist", "get"],  # /user/check_username_exist	# get	检查用户名是否已存在
    "check_email_exist&3": ["/user/check_email_exist", "get"],  # /user/check_email_exist	# get	注册时检查邮箱是否已存在
    "check_phone_exist&3": ["/user/check_phone_exist", "get"],  # /user/check_phone_exist	# get	注册时检查手机号是否已存在
    "check_email_belong_user&3": ["/user/check_email_belong_user", "get"],
    # /user/check_email_belong_user	# get	检查邮箱是否属于用户
    "/user/login&4": ["/user/login", "post"],  # /user/login	# post	用户账号(用户名/邮箱/手机号)密码登录
    "session_login&3": ["/user/session_login", "get"],  # /user/session_login	# get	设置session和cookie
    "register&4": ["/user/register", "post"],  # /user/register	# post	用户注册
    "temp_user&5": ["/user/temp_user", "put"],  # /user/temp_user	# put	临时用户账号登录
    "login_or_register_phone&4": ["/user/login_or_register_phone", "post"],
    # /user/login_or_register_phone	# post	手机号登录或注册
    "login_with_phone&4": ["/user/login_with_phone", "post"],  # /user/login_with_phone	# post	手机号登录
    "register_with_phone&4": ["/user/register_with_phone", "post"],  # /user/register_with_phone	# post	手机号注册
    "login_or_register_email&4": ["/user/login_or_register_email", "post"],
    # /user/login_or_register_email	# post	邮箱登录或注册
    "login_with_email&4": ["/user/login_with_email", "post"],  # /user/login_with_email	# post	邮箱登录
    "register_with_email&4": ["/user/register_with_email", "post"],  # /user/register_with_email	# post	邮箱注册
    "verify_code_phone&4": ["/user/verify_code_phone", "post"],  # /user/verify_code_phone	#post	验证手机验证码
    "reset_password_phone&4": ["/user/reset_password_phone", "post"],  # /user/reset_password_phone	#post	手机重置密码
    "verify_code_email&4": ["/user/verify_code_email", "post"],  # /user/verify_code_email	# post	验证邮箱验证码
    "reset_password_email&4": ["/user/reset_password_email", "post"],  # /user/reset_password_email	# post	邮箱重置密码
}

cources = {
    "course&3": ["/course", "get"],  # /course	get	个人课程/所有课程
    "course&5": ["/course", "put"],  # /course	put	管理员发布课程
    "series&3": ["/course/series", "get"],  # /course/series	get	学习路径的系列课程
    "individual&3": ["/course/individual", "get"],  # /course/individual	get	我的课程
    "comment&3": ["/course/comment/{course_id}", "get"],  # /course/comment/{course_id}	get	个人课程评分
    "rating&3": ["/course/rating/{course_id}", "get"],  # /course/rating/{course_id}	get	课程评分
    "rating&4": ["/course/rating/{course_id}", "post"],  # /course/rating/{course_id}	post	对参加的课程评分
    "status&3": ["/course/status", "get"],  # /course/status	get	课程状态 加入人数,完成人数
    "status&4": ["/course/status/{course_id}", "post"],  # /course/status/{course_id}	post	开始课程
    "tree&3": ["/course/tree/{course_id}", "get"],  # /course/tree/{course_id}	get	课程总览信息
    "grade&3": ["/course/grade/{course_id}", "get"],  # /course/grade/{course_id}	get	课程成绩信息
    "enroll&4": ["/course/enroll", "post"],  # /course/enroll	post	学习课程
    "course&4": ["/project/course", "post"],  # /project/course	post	获取或创建课程项目
}

