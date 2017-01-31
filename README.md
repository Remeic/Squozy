### Squozy

Squozy, it's all you need.
It's a link shortner, simple, fast and secure.
For every link we the solution!
*Share* your squozy link, and you're done!
**Only one click to generate a shortened url**

#### Extend Squozy to create your own custom shortner
Squozy love Django
##### Fork and clone it!
`git clone https://github.com/Remeic/Squozy.git`
##### Configure settings!

**private_settings.py**: Most important for your salt key
`SALT_KEY = "Your salt key"`

[**Heroku**](http://heroku.com/ "Heroku Website"): if you want deploy it on squozy:
rename *heroku_local_settings.py* to *local_settings.py*
got to your heroku dashboard, get database credential and paste on the correct field

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'take_it_from_heroku',
        'USER': 'take_it_from_heroku',
        'PASSWORD': 'take_it_from_heroku',
        'HOST': 'take_it_from_heroku',
        'PORT': 'take_it_from_heroku',
    }
}
```

Thanks to [Owanesh](https://github.com/Owanesh) for help me in troubleshooting