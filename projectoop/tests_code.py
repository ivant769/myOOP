from own_exception import MissingURL, DateImpossible

try:
    raise DateImpossible()
except DateImpossible as e:
    print(e.__class__.__name__)
    print(e)
