def task_install():
    """install """
    return {
        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* zappala@cs465.byu.edu:/var/www/cs465.byu.edu'],
#        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* clift@cs465.byu.edu:/var/www/cs465.byu.edu'],
#        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* seamons@cs465.byu.edu:/var/www/cs465.byu.edu'],        
        }
