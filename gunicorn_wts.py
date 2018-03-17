# Server Socket

# адрес и порт прослушивания
# значение по умолчанию ['127.0.0.1:8000']
bind = "127.0.0.1:8000"
# максимальное число ожидающих подключений
# значение по умолчанию 2048
backlog = 64

# Worker Processes

# число обработчиков
# значение по умолчанию 1
workers = 4
# тип обработчиков
# значение по умолчанию sync
# worker_class = "sync"

# число потоков на 1 обработчика
# указывается только для обработчиков типа gthread
# значение по умолчанию 1
# threads = 1

# максимальное число одновременно подключенных клиентов
# указывается для обработчиков типа eventlet и gevent
# значение по умолчанию 1000
# worker_connections = 1000

# количество обработанных обработчиком запросов перед его перезвпуском
# если 0, то перезапуск отключен
# значение по умолчанию 0
# max_requests = 0

# допустимое случайное отклонение от значения предыдущего параметра
# нужно для исключееия одновременной перезагрузки всех обработчиков
# значение по умолчанию 0
# max_requests_jitter = 0

# время ожилания отклика обработчика перед его насильственным закрытием
# значение по умолчанию 30
# timeout = 30

# время, выделяемое обработчику для плавного завершения
# значение по умолчанию 30
# graceful_timeout = 30

# время ожидания запроса для соединений типа keep alive
# обработчики типа sync эту опцию не воспринимают
# значение по умолчанию 2
# keepalive = 2

# Security options

# Максимальный размер http запроса в байтах
# значение по умолчанию 4094
# limit_request_line = 4094

# лимит по количеству заголовков в запросе
# значение по умолчанию 100
# limit_request_fields = 100

# максимальный размер http заголовка в байтах
# значение по умолчанию 8190
# limit_request_field_size = 8190

# Debugging options

# Опция управляет перезапуском обработчиков при изменении приложения
# Значение по умолчанию - False
reload = True

# менеджер перезагрузки обработчика ппи изменении приложения
# может быть auto, poll, inotify
# значение по умолчанию inotify
reload_engine = "auto"

# опция заставляет перезагружаться обработчик при изменении
# дополнмтельных файлов приложения ( шаблонов, конфигураций, и.т.д.)
# в качестве значения принимает список отслеживаемых файлов
# значение по умолчанию []
# reload_extra_files = []

# опция активизирует вывод каждой выполненной строки кода приложения в лог
# значение по умолчанию False
# spew = False

# проверить конфиг при запуске?
# опция использзуется при вызове gunicorn из командной строки
# для конфига не применима
# check_config

# Server mechanics options

# нужно ли прозводить предзагрузку приложений перед запуском обработчика?
# значение по умолчанию False
# preload_app = False

# запрет использования фукции sendfile()
# значение по умолчанию None
# sendfile = None

# установить флаг SO_REUSEPORT для прослушиваемого сокета
# значение по умолчанию False
# reuse_port = False

# опция позволяет изменить активную директорию перед загрузкой приложения
# chdir

# демон nизовать процесс
# значение по умолчанию False
# daemon = False

# опция позволяет установить значения для произвольных переменных окружения
# воспринимает список [“key=value"]
# raw_env = []

# имя файла, используемого в качестве pid
# значение по умолчанию None
# значение None обозначает неиспользование pid файла
# pidfile = None

# директория , используемая обработчиками в качестве временной
# значение по умолчанию None обозначает, что будет использована временная
# директория по умолчанию
# worker_tmp_dir = None

# пользователь, под которым запускаются обработчики
# в качестве значения указывается или имя пользователя или идентификатор
# пользователя
# значение None не приводит к изменению пользователя, под которым стартуют
# обработчики
user = "www-data"

# пользовательская группа, под которым запускаются обработчики
# в качестве значения указывается или имя группы или идентификатор
# группы
# значение None не приводит к изменению группы, от имени которой стартуют
# обработчики
group = "www-data"

# битовая маска прав доступа к файлам, создаваемым gunicorn
umask = 133

# разрешить доступ обработчика к файлам всех групп, к которым принадлежит
# пользователь
# значение по умолчанию False
# initgroups = False

# устаревающая опция
# можно не указывать
# tmp_upload_dir

# словарь, содержащий http загодовки, которые фронтенд использует для
# идентификации https запросов
# значение по умолчанию {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
# secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}

# ip фронтенда, с которого допустимо принимать защищенные запросы
# значение по умолчанию 127.0.0.1
# forwarded_allow_ips = "127.0.0.1"

# Logging

# путь к access.log файлу, используемого для сохранения истории обращений
# значение по умолчанию None
# значение "-" подразумевает логгирование в stdout
# accesslog = None

# запретить перенаправление лога доступа в syslog
# значение по умолчанию False
# disable_redirect_access_to_syslog = False

# формат лога доступа
# значение по умолчанию %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# файл лога ошибок
# значение по умолчанию "-" заставляет gunicorn производить логирование в stderr
# errorlog = "-"

# подробность логгирования
# значение по умолчанию info
# возможные варианты debug, info, warning, error, critical
# loglevel = info

# надо ли перенаправлять stdout/stderr в лог ошибок
# значение по умолчанию False
# capture_output = False

# логировщик, используемый для логирования событий в gunicorn
# значение по умолчанию gunicorn.glogging.Logger
# logger_class = gunicorn.glogging.Logger

# файл настроек для логировщика
# значение по умолчанию None
# logconfig = None

# словарь настроек для логировщика
# значение по умолчанию {}
# logconfig_dict = {}

# адрес по которому отправлять сообщения syslog
# значение по умолчанию udp://localhost:514
# syslog_addr = "udp://localhost:514"

# отправять логи gunicorn в syslog
# значение по умолчанию False
# syslog = False

# опция заставляет использовать значение параметра в качестве имени программы в записях syslog
# значение по умолчанию None
# syslog_prefix = None

# опция устанавливает тип программы для syslog
# значение по умолчанию user
# syslog_facility = user

# опция управляет включением/выключением наследования файловых дискрипторов для stdio в режиме демона
# значение по умолчанию False
# enable_stdio_inheritance = False

# host:port сервера statsd, в который отправляются логи
# значение по умолчанию  None
# statsd_host = None

# префикс, используемый для отправки статистики на сервер statsd
# если в значении параметра не указана лидирующая точка, то она дописывается автоматически
# значение по умолчанию ""
# statsd_prefix = ""

# Server Hooks

# hook - функция вызываемая при наступлении определенного события, например
#
# def on_exit(server):
#     pass
#
# on_starting
# on_reload
# when_ready
# pre_fork
# post_fork
# post_worker_init
# worker_int
# worker_abort
# pre_exec
# pre_request
# post_request
# child_exit
# worker_exit
# nworkers_changed
# on_exit

# Server Mechanics

# proxy_protocol
# proxy_allow_ips

# SSL

# keyfile
# certfile
# ssl_version
# cert_reqs
# ca_certs
# suppress_ragged_eofs
# do_handshake_on_connect
# ciphers

# Server Mechanics

# raw_paste_global_conf
