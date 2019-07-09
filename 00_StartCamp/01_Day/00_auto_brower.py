import webbrowser

asdf = ['남수경', '이현우', '강민구']

for idol in asdf:
    print(type(idol))
    webbrowser.open_new_tab('https://search.naver.com/search.naver?query='+idol)