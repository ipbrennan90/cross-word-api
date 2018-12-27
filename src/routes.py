class Router():
  @staticmethod
  def direct(class_type, request_type, params):
    if request_type == 'POST':
      return class_type.create(**params)
    if request_type == 'GET' and bool(params) :
      return class_type.show(**params)
    if request_type == 'GET' and not bool(params):
      return class_type.index()