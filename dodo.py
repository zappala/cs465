def task_install():
    """install """
    return {
#        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* zappala@cs465.byu.edu:/var/www/cs465.byu.edu'],
#        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* fred@cs465.byu.edu:/var/www/cs465.byu.edu'],
         #'actions': ['python app.py build','cp htaccess build/.htaccess','rsync --dry-run --exclude build/winter-2022 --exclude build/spring-2022 -rav build/* fred@cs465.byu.edu:/var/www/cs465.byu.edu'],
         'actions': ['python app.py build','cp htaccess build/.htaccess','rsync --exclude build/winter-2022 --exclude build/spring-2022 -rav build/* fred@cs465.byu.edu:/var/www/cs465.byu.edu'],
#        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync --exclude build/winter-2022 --exclude build/spring-2022 -rav build/* zappala@cs465.byu.edu:/var/www/cs465.byu.edu'],
#        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* seamons@cs465.byu.edu:/var/www/cs465.byu.edu'],        
        }
